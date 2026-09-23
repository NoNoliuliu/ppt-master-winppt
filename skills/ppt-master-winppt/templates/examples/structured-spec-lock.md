<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: zh-Hans-CN
- audience: 管理层
- objective: 用两页说明已核实的工作进展与下一步行动
- core_message: 结论先行，数据以已确认来源为准
- consumption_mode: presentation

## mode
- mode: briefing

## visual_style
- visual_style: minimal

## colors
- bg: #FFFFFF
- primary: #123B63
- accent: #E87722
- text: #1F2937
- secondary_text: #64748B
- divider: #D9E2EC

## typography
- font_family: Microsoft YaHei, Arial, sans-serif
- title_family: Microsoft YaHei, Arial, sans-serif
- body_family: Microsoft YaHei, Arial, sans-serif
- title: 30
- body: 16

## icons
- library: none
- inventory: none

## images
- brand_logo: images/brand_logo.png | source=user | crop=no-crop

## page_rhythm
- P01: anchor
- P02: dense

## pptx_structure
- mode: structured
- template_reuse_scope: layout
- template_adherence: adaptive

## pptx_masters
- win_3: 卫宁健康-深蓝色

## pptx_layouts
- win_3_1: win_3 | 01_cover | template:01_cover
- win_3_4: win_3 | 03_content | template:03_content

## page_pptx_layouts
- P01: win_3_1
- P02: win_3_4

## page_layouts
- P01: 01_cover
- P02: 03_content

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
