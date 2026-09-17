import numpy as np

def point_in_polygon(x, y, poly_x, poly_y):
    """
    Determine if a point is inside a polygon using ray casting algorithm.
    """
    n = len(poly_x)
    inside = False

    p1x, p1y = poly_x[0], poly_y[0]
    for i in range(1, n + 1):
        p2x, p2y = poly_x[i % n], poly_y[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

def classify_soil_texture(sand_pct, silt_pct, clay_pct):
    """
    Classify soil texture based on USDA soil texture triangle.
    Returns the textural class name.
    """
    # Ensure values sum to 100
    total = sand_pct + silt_pct + clay_pct
    if abs(total - 100.0) > 0.5:
        # Normalize
        sand_pct = (sand_pct / total) * 100
        silt_pct = (silt_pct / total) * 100
        clay_pct = (clay_pct / total) * 100

    # Define boundaries for each texture class in the USDA triangle
    # Format: [sand_min, sand_max, clay_min, clay_max] or more complex polygons
    texture_classes = {
        'Sand': {
            'polygon': ([85, 90, 100, 100, 85], [0, 0, 0, 4, 0])
        },
        'Loamy Sand': {
            'polygon': ([70, 85, 85, 90, 70], [0, 0, 4, 10, 0])
        },
        'Sandy Loam': {
            'polygon': ([52.5, 70, 85, 80, 52.5], [7, 0, 0, 20, 20])
        },
        'Loam': {
            'polygon': ([22.5, 52.5, 52.5, 27.5, 20], [27.5, 20, 45, 55, 45])
        },
        'Silt Loam': {
            'polygon': ([0, 27.5, 27.5, 0, 0], [50, 55, 80, 100, 50])
        },
        'Silt': {
            'polygon': ([0, 0, 20, 0], [80, 100, 100, 80])
        },
        'Sandy Clay Loam': {
            'polygon': ([45, 52.5, 52.5, 45], [27.5, 20, 40, 45])
        },
        'Clay Loam': {
            'polygon': ([20, 45, 45, 27.5, 20], [45, 45, 60, 72.5, 55])
        },
        'Silty Clay Loam': {
            'polygon': ([0, 20, 20, 0], [45, 55, 60, 45])
        },
        'Sandy Clay': {
            'polygon': ([45, 65, 65, 45], [35, 35, 55, 55])
        },
        'Silty Clay': {
            'polygon': ([0, 20, 20, 0], [60, 60, 100, 100])
        },
        'Clay': {
            'polygon': ([20, 45, 45, 20], [55, 55, 100, 100])
        }
    }

    # Check each class in order
    for texture_class, data in texture_classes.items():
        poly_x, poly_y = data['polygon']
        if point_in_polygon(sand_pct, clay_pct, poly_x, poly_y):
            return texture_class, (sand_pct, silt_pct, clay_pct)

    # Default to "Unknown" if no match
    return "Unknown", (sand_pct, silt_pct, clay_pct)

def get_texture_boundaries():
    """
    Return the boundaries for all texture classes.
    """
    texture_classes = {
        'Sand': ([85, 90, 100, 100, 85], [0, 0, 0, 4, 0]),
        'Loamy Sand': ([70, 85, 85, 90, 70], [0, 0, 4, 10, 0]),
        'Sandy Loam': ([52.5, 70, 85, 80, 52.5], [7, 0, 0, 20, 20]),
        'Loam': ([22.5, 52.5, 52.5, 27.5, 20], [27.5, 20, 45, 55, 45]),
        'Silt Loam': ([0, 27.5, 27.5, 0, 0], [50, 55, 80, 100, 50]),
        'Silt': ([0, 0, 20, 0], [80, 100, 100, 80]),
        'Sandy Clay Loam': ([45, 52.5, 52.5, 45], [27.5, 20, 40, 45]),
        'Clay Loam': ([20, 45, 45, 27.5, 20], [45, 45, 60, 72.5, 55]),
        'Silty Clay Loam': ([0, 20, 20, 0], [45, 55, 60, 45]),
        'Sandy Clay': ([45, 65, 65, 45], [35, 35, 55, 55]),
        'Silty Clay': ([0, 20, 20, 0], [60, 60, 100, 100]),
        'Clay': ([20, 45, 45, 20], [55, 55, 100, 100])
    }
    return texture_classes

def create_ternary_plot(sand_pct, silt_pct, clay_pct, classification):
    """
    Create a ternary plot showing the USDA soil texture triangle with the sample point.
    """
    import plotly.graph_objects as go
    
    # Get texture boundaries
    texture_classes = get_texture_boundaries()
    
    fig = go.Figure()

    # Add each texture class polygon
    for texture, (x_coords, y_coords) in texture_classes.items():
        fig.add_trace(go.Scatter(
            x=x_coords,
            y=y_coords,
            fill='toself',
            mode='lines',
            name=texture,
            hovertemplate=f'{texture}<extra></extra>',
            line=dict(width=1),
            opacity=0.6
        ))

    # Add the sample point
    fig.add_trace(go.Scatter(
        x=[sand_pct],
        y=[clay_pct],
        mode='markers',
        marker=dict(size=12, color='red', symbol='x'),
        name='Sample Point',
        hovertemplate=f'Sample: Sand={sand_pct:.1f}%, Clay={clay_pct:.1f}%<br>Classification: {classification}<extra></extra>'
    ))

    fig.update_layout(
        title='USDA Soil Texture Triangle',
        xaxis_title='Sand (%)',
        yaxis_title='Clay (%)',
        showlegend=True,
        width=600,
        height=600,
        xaxis=dict(range=[0, 100]),
        yaxis=dict(range=[0, 100])
    )
    
    return fig
