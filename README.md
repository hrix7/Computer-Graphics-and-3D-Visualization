# Computer Graphics and 3D Visualization

I completed Stanford University's Summer Session in Computer Graphics and Imaging from June to August 2025. This repository documents the graphics foundations I used to build and render my final scene and connects that work with my broader interest in biomedical visualization.

## Work I completed

- Built a complete final scene for the course.
- Worked with object placement, model transformations, materials, lighting, and camera composition.
- Applied translation, rotation, and scaling through homogeneous transformation matrices.
- Adjusted the camera and perspective to frame the scene.
- Evaluated how surface and lighting choices changed depth, appearance, and readability.
- Organized the project so the graphics methods can later support anatomical and medical-device visualization.

## Repository code

- `src/transforms.py` implements translation, scaling, Z-axis rotation, and point transformation.
- `src/camera.py` implements look-at and perspective-projection matrices.
- `examples/scene_manifest.yaml` demonstrates how scene assets can be organized.
- `docs/ASSET_POLICY.md` records the rules I follow before publishing models or textures.

## Run the examples

```bash
python -m pip install -r requirements.txt
python src/transforms.py
python src/camera.py
```

## Tools and concepts

Computer graphics, rendering, lighting, materials, scene composition, Blender, Python, NumPy, 3D visualization.

## Public materials

Only original or permission-cleared assets should be committed. Course-provided assets and copyrighted textures are not redistributed.

## Author and Project Setting

**Author:** Hritika Adhikary  
**Program:** Computer Graphics and Imaging Summer Session  
**Institution:** Stanford University, Palo Alto, California  
**Period:** June - August 2025

## Rights

Copyright (c) 2026 Hritika Adhikary. All rights reserved. See [LICENSE](LICENSE).
