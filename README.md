# win-ppt

基于 [Hugo He / PPT Master](https://github.com/hugohe3/ppt-master) v6.6.0 的本地改编版，保留四套卫宁健康模板及个性化工作规则。

## 获取与安装

下载本仓库 ZIP 并解压，将 `skills/win-ppt` 整个文件夹放入所用 AI 工具支持的 Skill 目录，然后重新加载 Skill。也可克隆本仓库；运行时需使用 Skill 所在目录的绝对路径。

运行环境为 Python 3.10+，按 `skills/win-ppt/requirements.txt` 安装对应依赖。不同功能的额外依赖见其工作流说明。内置 `lib` 是历史 Windows CPython 3.13 依赖，不适用于其他平台或 Python 版本，不能代替全部新版依赖。

API 凭据通过进程环境变量提供，或用 `WIN_PPT_ENV_FILE` 指定本地配置文件。不要把实际配置或凭据提交到 GitHub。

## 保留的改编

- 四套模板：AI汇报、橘色、深蓝色、暖调大地色，保留Logo与背景。
- 默认复制导入，保留原文件。
- 沿用明确的模板选择；设计确认后连续逐页执行，避免重复询问。
- 允许必要的图片检查；每页读取锁定设计规范。
- 完整本地规则见 [win-local.md](skills/win-ppt/references/win-local.md)。

## 分享版与本地2.0.0的区别

这是 win-ppt 2.0.0 的分享整理版：移除两份包含固定本机路径和未核实医院示例数字的历史生成脚本，移除个人部署标记；保留核心生成流程与品牌模板。未包含升级备份、审计日志或测试输出。分享仓库独立于原作者项目，不代表官方发布。

## 验证范围

四套模板20页SVG与旧版渲染逐像素一致；模板导出、项目导入和本地兼容测试通过。Windows实机、真实PowerPoint显示及付费生图/语音API尚未验证；请先在目标环境试运行。以上测试范围不能视为所有上游功能均已实测。

## 来源与许可

上游版本和提交见 [upstream-lock.json](skills/win-ppt/upstream-lock.json)。保留上游MIT许可证、归属信息及第三方依赖许可证。卫宁健康Logo、商标及公司模板保留其原有权利归属，代码许可证不构成商标授权。
