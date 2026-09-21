# win-ppt Local Customization Contract

Read this file at entry. These local rules override conflicting defaults in the imported PPT Master runtime; keep its schema, quality checks, attribution, and export implementation intact.

## 1. Identity and template choice

Keep the invocation name `win-ppt`. Default Generate offers these local templates first: `卫宁健康-AI汇报`, `卫宁健康-橘色`, `卫宁健康-深蓝色`, `卫宁健康-暖调大地色`. Their original files remain under `templates/layouts/`; their registered v6.6-compatible workspaces are under `templates/decks/`. Read `templates/win-layouts-index.json` for the four choices. Other upstream templates and free design remain available on explicit request.

Default Generate uses chat confirmation unless the user requests the browser UI. In Step 3 prepare the four local choices; in Stage 1 use `templates` as the default mode and require an explicit choice before installation. Reuse an exact choice already supplied for this task. Do not silently default to free design, select a template for the user, or ask them to approve the same choice twice. Stage 1 also retains the upstream communication fields; after it closes, install the selected modern workspace with `apply_template.py` before preparing Stage 2.

## 2. Approval and continuity

Retain two approval points for ordinary Default generation: template/communication choice, then the complete design recommendation. Stage 2 includes all eight legacy decisions (canvas, page range, audience, style, colors, icons, typography, images) together with the additional upstream fields. Reuse confirmed facts. Existing decisions are not permission to skip a missing required choice.

After final design approval, continue through Design Spec, lock, resources, SVG pages, notes, validation, and export without routine approval questions. Checkpoints and the Executor parameter listing are internal verification or progress notices. Ask again only for a material deviation, a new required decision, or an expressly requested design review. Optional `refine_spec` stays off unless requested. The approved default is one continuous run with sequential pages; do not split into batches or delegate SVG generation. Read the current `spec_lock.md` before each page in Default mode. Keep approved colors, typography, icons, and image assets; resolve a needed new anchor in the spec before using it.

Explicit Quick/skip-strategy instructions can select the upstream Quick runtime as a user-directed exception. A request merely to make a PPT, use a local template, or improve quality does not authorize Quick or waive the local approval points. Image reconstruction and native editing retain their own route contracts; do not misroute an existing-deck edit through Default Generate.

## 3. Source and visual preservation

Import with explicit `--copy`; relocate originals only when the user expressly requests it. The compatibility CLI also defaults to copying files inside scratch/project directories. Use an explicit output project path outside the managed Skill installation (`project_manager.py init ... --dir <workspace>`).

Preserve the selected local template's logos, background assets, palette, typography, and visual character. Keep source media and original templates unchanged. Inspect images when necessary to identify content, verify a logo, place a crop, or check the finished result. Metadata analysis alone does not prove visual fidelity. Use equivalent host tools when a named file-reading or question tool is unavailable; this never removes an approval requirement.

Before running commands, resolve a native Python 3.10+ interpreter with the dependencies required by the selected route (`requirements.txt`). For core template/export work this includes PyYAML, Pillow, lxml and python-pptx. Treat `python3` in upstream examples as that resolved interpreter. The preserved `lib/` bundle is Windows CPython 3.13 only; never prepend it on macOS/Linux.

## 4. Local compatibility tools

| Existing capability | Maintained entry |
|---|---|
| List four local templates | `scripts/project_manager.py list-templates` |
| Import a local template | `scripts/project_manager.py import-template <project_path> <template_name>`; installs the registered modern workspace |
| Export wrapper | `scripts/run_svg_to_pptx.py`; uses the current exporter and native host dependencies |
| Original Windows PowerPoint reference import and selection report | `scripts/win_pptx_template_import.py`; opt-in legacy route, original CLI options preserved |
| Externalize inline pictures / optimize reference SVGs | `scripts/template_import/externalize_images.py`, `scripts/template_import/optimize_reference.py` |
| Negative image prompt compatibility | `scripts/image_gen.py "prompt" --negative_prompt "items to avoid"`; the avoid instruction is appended for the selected backend; manifest items put it directly in each prompt |

For an explicitly requested legacy reference-import workflow, read [the retained runbook](win-legacy/create-template.md). It retains reference-page selection, canonical asset naming, helper/mask exclusion, `normalized_assets.json`, full selected-page inspection, and placeholder naming. Its output is a legacy template; to enter the new runtime, adapt it to the current workspace contract rather than passing legacy output to the new checker as if it were already modern.

When creating a modern template from imported material, preserve those semantic checks using the new importer artifacts: review the selected source pages, distinguish canonical assets from masks/derived helpers, give retained assets meaningful names, and retain the review mapping in the project analysis directory. The new importer owns its file schema; never fabricate legacy or modern provenance receipts. The current Create Template workflow owns export and registration.

Image configuration keeps process environment precedence and the old repository-root `.env` fallback. `WIN_PPT_ENV_FILE` can explicitly select a project config. Do not silently read `~/.ppt-master/.env` or package credentials inside a Skill.

## 5. Managed upgrades

This is a maintained adaptation of `https://github.com/hugohe3/ppt-master`, pinned to upstream v6.6.0 / `a50758ac29ec027e85966db33e2ae80031446756`; local version 2.0.0 is independent. Keep the MIT license, author identity, and attribution checks. Upgrade in an isolated candidate, preserve this contract and all local template assets, validate, then obtain the registry-required publication approval. Use `obsidian-skill-registry` to publish and sync; never update a deployed copy by pulling upstream in place.
