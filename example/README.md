# Example / 示例

一份端到端的示例报告样张，演示 LedgerGauge 完整输出长什么样。

An end-to-end sample deliverable showing what a complete LedgerGauge report looks like.

| File | 说明 / Description |
|------|------|
| [`sample_report.md`](sample_report.md) | 基于虚构案例 **MapleLeaf BioFoundry** 的完整可行性报告，含还款表、三层营收确认、双口径 P&L/FCF、保守 vs 乐观情景对比、敏感性分析与结论 |

报告里的每一个名字与数字都是虚构的，由仓库根目录的 `assets/sample_input.json` 经
`scripts/fin_model.py` 计算得到，与任何真实项目无关。要自己复现：

Every name and figure is fictional, computed from `assets/sample_input.json` via
`scripts/fin_model.py`. To reproduce:

```bash
python scripts/fin_model.py --input assets/sample_input.json --output result.json
```

> 仅用于演示，不构成投资或融资建议。/ For demonstration only; not investment or financing advice.
