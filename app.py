import gradio as gr
import plotly.graph_objects as go
from usda_soil_texture_triangle_classifier import classify_soil_texture, get_texture_boundaries, create_ternary_plot

def process_classification(sand_pct, silt_pct, clay_pct):
    if sand_pct is None or silt_pct is None or clay_pct is None:
        return "Error: All values must be provided.", None
    
    # Validate inputs
    if sand_pct < 0 or silt_pct < 0 or clay_pct < 0:
        return "Error: All percentages must be non-negative.", None
    if sand_pct > 100 or silt_pct > 100 or clay_pct > 100:
        return "Error: All percentages must be between 0 and 100.", None
    
    total = sand_pct + silt_pct + clay_pct
    original_values = [sand_pct, silt_pct, clay_pct]
    
    # Check if values sum to 100 within tolerance
    if abs(total - 100.0) > 0.5:
        # Normalize values
        normalized_sand = (sand_pct / total) * 100
        normalized_silt = (silt_pct / total) * 100
        normalized_clay = (clay_pct / total) * 100
        result, normalized = classify_soil_texture(normalized_sand, normalized_silt, normalized_clay)
        note = f"Note: Values were normalized from ({sand_pct:.1f}, {silt_pct:.1f}, {clay_pct:.1f}) to ({normalized_sand:.1f}, {silt_pct:.1f}, {clay_pct:.1f}) to sum to 100."
        fig = create_ternary_plot(normalized_sand, normalized_silt, normalized_clay, result)
        return f"{result}\n{note}", fig
    else:
        result, _ = classify_soil_texture(sand_pct, silt_pct, clay_pct)
        fig = create_ternary_plot(sand_pct, silt_pct, clay_pct, result)
        return result, fig

with gr.Blocks() as demo:
    gr.Markdown("## USDA Soil Texture Triangle Classifier")
    with gr.Row():
        with gr.Column():
            sand_input = gr.Number(label="Sand %")
            silt_input = gr.Number(label="Silt %")
            clay_input = gr.Number(label="Clay %")
            classify_btn = gr.Button("Classify")
            gr.Markdown("Values should sum to 100%")
        
        with gr.Column():
            result_output = gr.Textbox(label="USDA Textural Class")
            plot_output = gr.Plot(label="Soil Texture Triangle")

    classify_btn.click(
        fn=process_classification,
        inputs=[sand_input, silt_input, clay_input],
        outputs=[result_output, plot_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
