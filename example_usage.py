from client import SpatialSemanticInteriorDesignLayoutSynthesizerClient

def main():
    client = SpatialSemanticInteriorDesignLayoutSynthesizerClient()
    res = client.synthesize_room_layout('EXECUTIVE_HOME_OFFICE', {'length': 4.5, 'width': 4.0, 'height': 3.0}, 'MID_CENTURY_MODERN')
    print('Interior Layout Synthesizer: ' + res['interior_plan_id'] + ' (' + res['aesthetic_theme'] + ')')
    print('Furniture Pieces: ' + str(res['furniture_pieces_placed_count']) + ' | Ergonomics: ' + str(res['spatial_clearance_ergonomic_score_pct']) + '%')
    print('Floorplan SVG: ' + res['isometric_floorplan_svg_url'])
    print('Photorealistic Render: ' + res['photorealistic_render_webp_url'])

if __name__ == '__main__':
    main()
