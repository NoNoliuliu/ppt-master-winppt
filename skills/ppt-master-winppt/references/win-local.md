# ppt-master-winppt Local Customization Contract

Read this file at entry. These local rules override conflicting defaults in the imported PPT Master runtime; keep its schema, quality checks, attribution, and export implementation intact.

## 1. Identity and template choice

Keep the invocation name `ppt-master-winppt`. Default Generate offers these local templates first: `卫宁健康-AI汇报`, `卫宁健康-橘色`, `卫宁健康-深蓝色`, `卫宁健康-暖调大地色`. Their original files remain under `templates/layouts/`; their registered v6.6-compatible workspaces are under `templates/decks/`. Read `templates/win-layouts-index.json` for the four choices. Other upstream templates and free design remain available on explicit request.

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

This is a maintained adaptation of `https://github.com/hugohe3/ppt-master`, pinned to upstream v6.6.0 / `a50758ac29ec027e85966db33e2ae80031446756`; local version 2.1.0 is independent. Keep the MIT license, author identity, and attribution checks. Upgrade in an isolated candidate, preserve this contract and all local template assets, validate, then obtain the registry-required publication approval. Use `obsidian-skill-registry` to publish and sync; never update a deployed copy by pulling upstream in place.

## Environment preflight

After the attribution guard succeeds, run the environment check at the start of every task using the exact interpreter that will run subsequent scripts. Repeat if that interpreter changes. A previous success on the same machine is not sufficient.

1. Resolve Python 3.10+ from the host's actual runtime configuration. WorkBuddy may supply a managed virtual environment, but its path is machine-specific: never assume a fixed `~/.workbuddy/binaries/...` path. Record the absolute interpreter and use it consistently for guard, bootstrap, preview and export. Do not substitute an unrelated `python` or `pip` command later.
2. Run `"<python>" "<skill-dir>/scripts/bootstrap_env.py" --check-only`. Exit 0 means the PPT-profile packages import successfully and declared minimum versions are met. Exit 1 means core dependencies are missing/unusable. Exit 2 means unsupported Python or a check failure; resolve it before continuing.
3. For exit 1, select a writable host-approved venv or create a dedicated project venv outside the managed Skill directory. Run the bootstrap without `--check-only` using that venv's interpreter. It installs only unavailable core packages and rechecks them in a fresh process. Follow host permissions; never elevate into system Python, use sudo pip, or bypass an externally managed environment. No need to repeat the user's presentation design approval for routine authorized dependency setup.
4. The default `--profile ppt` checks the template/export baseline (PyYAML, python-pptx, lxml, Pillow, XlsxWriter). Continue this route after exit 0. Check/install Flask separately with `--profile preview`; its failure only disables browser preview/confirmation UI, not PPT generation. This check is not proof that every optional route is ready: consult the chosen route and `requirements.txt` for its extra packages, external tools, fonts and API configuration. Install only extras required by the requested route.

macOS/Linux example (replace placeholders with actual absolute paths):

```sh
"<python>" "<skill-dir>/scripts/bootstrap_env.py" --check-only
"<python>" -m venv "<project-dir>/.venv-ppt"
"<project-dir>/.venv-ppt/bin/python" "<skill-dir>/scripts/bootstrap_env.py"
```

Windows PowerShell equivalent (no activation or execution-policy change needed):

```powershell
& "<python.exe>" "<skill-dir>/scripts/bootstrap_env.py" --check-only
& "<python.exe>" -m venv "<project-dir>/.venv-ppt"
& "<project-dir>/.venv-ppt/Scripts/python.exe" "<skill-dir>/scripts/bootstrap_env.py"
```

Use an existing approved venv instead of creating one when available. Pip inherits the chosen environment's standard configuration (`pip.ini`/`pip.conf`, `PIP_INDEX_URL`, proxy settings). Use only the organization's supplied mirror/proxy values; never invent an internal URL, commit credentials, disable TLS, or copy credential-bearing pip output into chat. Installation failure is exit 2 for the selected profile only. A failed PPT baseline blocks that dependent route; a failed preview profile does not block export.

### Capability degradation: preserve the requested PPT deliverable

Attempt preview setup by running `bootstrap_env.py --profile preview` with the approved venv before its first use. If installation or service startup fails, report that browser preview is unavailable, use chat for confirmations, and continue PPT generation when its dependencies are ready. Do not repeatedly retry a failed optional installation. If preview starts, report its actual URL and health result; never claim browser-level validation from imports alone.

Do not make narration, animation or other optional enhancements prerequisites for a basic PPT. On optional failure, disclose the omitted feature and continue a usable basic deck when the user's requirements permit. If the user explicitly makes a feature mandatory, pause only that dependent delivery instead of silently dropping it. Preserve existing content and confirmations.

Missing source-conversion dependencies may be bypassed only when equivalent complete source content is actually available (for example, user-supplied text instead of a DOCX conversion). Never omit unread material, invent text, or bypass source/quality/attribution checks to claim a successful minimal PPT. Do not substitute unsupported SVG effects merely to require additional packages; use a supported simpler layout when consistent with the approved design.

### Windows execution and incomplete-package diagnostics

On Windows, use the host's working PowerShell with an absolute Python executable and quoted absolute script/project paths. Do not depend on Bash, `dirname`, `ls`, `python3`, or Unix path conversion. If those commands fail or produce paths such as `c:\c\Users`, stop retrying that command style and resolve the actual Windows paths. Do not change global PATH or execution policy to run this Skill.

For bootstrap diagnostics use `--report "<project-dir>/bootstrap-report.txt"`; it writes UTF-8 directly via Python and returns the same check status. For other tools whose captured output is empty/garbled, use Python `subprocess.run` with argument lists and write the captured bytes to a diagnostic file using explicit decoding/UTF-8 encoding, then inspect both the exit code and file. PowerShell redirection can use UTF-16 depending on version; do not infer command success from an empty console. Keep credentials out of logs.

Bootstrap reports the presence of the export entry, checker, confirmation UI and preview server independently of pip dependencies. A missing Skill component requires restoring the correct complete package, not installing Flask. Missing optional UI permits chat confirmation; missing preview permits basic PPT export. Never invent a legacy `modes/visual-styles` path: use the installed route and Executor references. Capture the Skill version, interpreter and exact failed path when reporting an incomplete installation.

### Optional backup compatibility

Native editable PPTX is the basic delivery. An optional SVG/image backup requiring PNG fallback is a separate capability: if raster dependencies fail, disclose the omitted backup and deliver the valid native PPTX. Do not call an SVG-only backup compatible with the recipient's Office version without testing; CairoSVG also requires a working native Cairo runtime, so successful pip installation alone is not proof of raster readiness.
