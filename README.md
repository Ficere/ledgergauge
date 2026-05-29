# 📐 LedgerGauge / 债务融资版平台可行性测算

为债务驱动建设的重资产服务/研发平台（共享实验室、CRO/foundry 平台、中试基地、设备密集型业务）构建可行性财务模型，并产出配套的可行性报告。一次回答两个问题：**能不能创造价值（会计利润）** 与 **能不能扛过还款（自由现金流）**。

Build a debt-financed feasibility model — and write the matching report — for any capital-intensive service or R&D platform. It answers two questions side by side: **can it create value (accounting P&L)** and **can it survive repayment (free cash flow under the debt schedule)**.

遵循 [Agent Skills 开放标准](https://agentskills.io)，兼容 Claude Code、Cursor、GitHub Copilot、Codex、Windsurf、Gemini CLI、Perplexity Computer 等 30+ AI Agent 平台。

![License](https://img.shields.io/badge/license-MIT-blue) ![Python](https://img.shields.io/badge/python-3.x-green) ![No deps](https://img.shields.io/badge/dependencies-none-lightgrey)

## 安装 / Install

```bash
npx skills add Ficere/ledgergauge
```

> 需要 Node.js。安装后 Agent 会自动发现并按需加载该技能。
>
> Requires Node.js. Once installed, your agent auto-discovers and loads this skill when relevant.

<details>
<summary>其他安装方式 / Alternative methods</summary>

**手动安装 / Manual install：**

```bash
git clone https://github.com/Ficere/ledgergauge.git
# 将整个目录复制到你的 Agent 的 skills 目录下即可
# Copy the directory to your agent's skills folder:
#   Claude Code:  ~/.claude/skills/
#   Cursor:       .cursor/skills/
#   Copilot:      .github/skills/
#   Codex:        ~/.codex/skills/
#   Gemini CLI:   .gemini/skills/
```

**Perplexity Computer：**

下载本仓库 zip → 在 [Skills 管理页面](https://www.perplexity.ai/computer/skills) 上传。

</details>

## 使用 / Usage

安装后用自然语言触发，无需任何配置：

```
帮我给这个共享实验室平台做一份债务融资版的财务可行性测算，建设投入靠借款，需要还款压力测试和回本分析
```

```
我们要建一个 CRO foundry 平台，CapEx 用贷款覆盖。营收分三层：稳定的检测服务、合作开发分成、技术授权。帮我跑乐观和保守两套口径，看现金流低点会不会击穿
```

```
对这个中试基地的测算做敏感性分析，看毛利率、授权概率、利率谁对现金流低点影响最大
```

```
把测算结果写成一份可行性报告，会计利润和自由现金流两条线分开讲
```

## 功能 / Features

| 模块 / Module | 说明 / What it does |
|------|------|
| **还款压力测试 / Debt stress test** | 等额本息摊销表，逐年还本付息，作为现金流的硬约束 |
| **三层营收 / 3-layer revenue** | A 稳定经常性收入、B 合作开发（风险调整）、C 技术授权（高波动）分层建模 |
| **双口径核算 / Dual-caliber accounting** | 同时输出会计 P&L（价值）与自由现金流 FCF（生存），两条线分开看 |
| **情景分析 / Scenarios** | 保守 vs 乐观，二者仅在「波动性授权层 C 如何确认」上不同，其余假设完全一致 |
| **敏感性分析 / Sensitivity** | 对现金流低点（cash trough）做单因子（OAT）扰动，识别最致命的变量 |
| **独立引擎 / Standalone engine** | 纯 Python 3、零第三方依赖，可脱离 Agent 平台独立运行 |
| **报告模板 / Report template** | 内置可行性报告结构，会计利润与还款生存两条主线分述 |

<details>
<summary>三层营收口径 / The three revenue layers</summary>

| 层 / Layer | 性质 / Nature | 确认方式 / Recognition |
|------|------|------|
| **A — 经常性 / Recurring** | 稳定服务收入，可预测 | 按预测全额计入 |
| **B — 合作开发 / Co-development** | 里程碑分成，中等风险 | 风险调整后计入（避免过度前置） |
| **C — 技术授权 / IP licensing** | 高单价、高波动、低频 | 保守口径按概率加权，乐观口径全额计入 |

价值定价（value-based），非成本加成（cost-plus）。里程碑收入遵守纪律，不过度前置确认。

</details>

<details>
<summary>情景设计原则 / Scenario design principle</summary>

保守与乐观两套情景 **唯一** 的区别在于 Layer C（技术授权）的确认方式：

- **保守 / Conservative**：授权收入按成功概率加权确认（prob-weighted）
- **乐观 / Optimistic**：授权收入按预期全额确认（full recognition）

A 层、B 层、成本、利率、还款表、营运资金等所有其他假设两套情景完全一致。这样设计的目的是：让两套结果的差异 **完全可归因** 于最不确定的那一层收入，而不是一堆假设同时变动造成的混沌。

</details>

## 独立脚本 / Standalone Script

`scripts/fin_model.py` 可脱离 Agent 平台独立运行（Python 3，无第三方依赖）：

```bash
python scripts/fin_model.py --input assets/sample_input.json --output result.json
```

引擎会输出：摊销表、三层营收的双口径确认、逐年 P&L 与 FCF、保守/乐观两套情景的盈亏平衡年与回本年、现金流低点（trough），以及对低点的单因子敏感性。

<details>
<summary>输入 JSON 示例 / Sample input（虚构案例 / fictional example）</summary>

仓库自带 `assets/sample_input.json` 是一个完全虚构的示例 **MapleLeaf BioFoundry**（单位 kUSD，本金 8400、利率 3.2%、8 年期），与任何真实项目无关，仅用于演示引擎用法：

```json
{
  "name": "MapleLeaf BioFoundry",
  "currency_unit": "kUSD",
  "debt": { "principal": 8400, "annual_rate": 0.032, "years": 8 },
  "layer_a": [620, 1480, 2510, 3360, 3980, 4420, 4710, 4880],
  "layer_b": [0, 60, 180, 340, 520, 640, 760, 880],
  "layer_c": { "unit_price": 1100, "projects": [0,0,1,2,2,3,3,3], "success_prob": 0.35 },
  "gross_margin": { "a": 0.48, "b": 0.58, "c": 0.82 },
  "opex": [760, 1080, 1480, 1780, 1940, 2040, 2110, 2150],
  "depreciation": [560, 880, 1040, 1040, 1040, 1040, 1040, 1040],
  "working_capital_ratio": 0.05
}
```

运行该示例的概要结果（虚构）：还款年供约 1191.5 kUSD；保守口径现金流低点出现在第 5 年（约 −5309），乐观口径低点出现在第 3 年（约 −3830），第 7 年回本。敏感性上，A 层毛利率对现金流低点的影响最大。

</details>

## 目录结构 / Structure

```
ledgergauge/
├── SKILL.md                      # 技能入口（Agent 自动读取）
├── scripts/
│   └── fin_model.py              # 独立测算引擎（纯 Python，无依赖）
├── references/
│   ├── revenue_layers.md         # 三层营收建模口径
│   ├── dual_caliber.md           # 会计 P&L 与自由现金流双口径定义
│   ├── scenarios.md              # 保守/乐观情景设计原则
│   ├── sensitivity.md            # 单因子敏感性分析框架
│   ├── report_template.md        # 可行性报告结构模板
│   └── worked_example.md         # 端到端虚构示例走查
├── assets/
│   └── sample_input.json         # 虚构示例输入（MapleLeaf BioFoundry）
├── LICENSE                       # MIT
└── README.md
```

## 免责声明 / Disclaimer

本技能为财务建模与情景测算的 **方法论工具**，所有内置数字与案例（含 MapleLeaf BioFoundry）均为虚构，仅用于演示。其输出 **不构成投资建议、融资建议或财务保证**，不应替代专业的财务、税务、法律或审计意见。实际决策请咨询有资质的专业人士，并以经核验的真实数据为准。

This skill is a **methodology tool** for financial modeling and scenario analysis. All built-in figures and cases (including MapleLeaf BioFoundry) are fictional and for illustration only. Its output is **not investment, financing, or financial advice** and is no substitute for professional financial, tax, legal, or audit counsel. Consult qualified professionals and use verified real data for any actual decision.

## License

MIT —— 详见 [LICENSE](LICENSE)。
