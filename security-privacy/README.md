# FuXi 安全与隐私保护体系

**FuXi Security & Privacy Program**

> 面向全球用户。本体系用于清晰、真实、完整地说明 FuXi 如何保护你的数据与安全，
> 以及我们对你的承诺。**FuXi 本质安全、保护用户，尊重全球法律与用户行为** ——
> 这一原则由架构而非口号实现。

---

## 为什么你可以信任 FuXi

FuXi 从设计之初就把"不收集、不窥探、由你掌控"作为默认状态，而不是事后追加的条款：

- **本地优先（Local-first）**：FuXi 运行在你的机器上，配置、会话、检查点都存储在本地 `~/.fuxi/`（可用 `FUXI_CONFIG_DIR` 覆盖），默认不上传到任何 FuXi 服务器。
- **自带密钥（Bring your own key）**：你可以使用任意提供商（OpenAI 兼容、Gemini、Bedrock/Vertex 等）的 API Key，代码与对话直接发往你选择的模型提供商，不经过 FuXi。
- **凭据由你持有**：API Key 只保存在你的本地配置中，FuXi 不复制、不上传你的密钥。
- **命令安全护栏**：shell 命令在执行前经过 AST 安全分类器与规则集过滤；配合细粒度权限与操作审计，自主执行始终在你的掌控之中。
- **可验证的更新**：`fuxi update` 对下载的二进制做 SHA-256 校验和验证，并原子性替换，杜绝被篡改的安装。

**最重要的一句话：** 默认情况下，FuXi 不要求注册、不要求登录，你的代码和对话内容不会被收集进 FuXi 的服务器。

---

## 体系结构（六层）

本体系采用分层治理结构，从原则到执行逐级细化，覆盖完整的组织级安全与隐私治理：

```
L0  治理 Governance       —— 最高目标与治理机制
L1  政策 Policies         —— "必须做什么"（规范性）
L2  标准 Standards        —— "如何做到"（技术规范）
L3  流程 Procedures       —— "一步步怎么做"（操作手册）
L4  合规 Compliance       —— 对照全球法律的映射
L5  信任 Trust            —— 面向用户的可信披露
```

---

## 文档目录

### 核心文档（入口）

| 文档 | 内容 | English |
|---|---|---|
| [隐私政策](PRIVACY_POLICY.zh-CN.md) | 我们收集什么、不收集什么、数据如何流动 | [Privacy Policy](PRIVACY_POLICY.md) |
| [安全白皮书](SECURITY.zh-CN.md) | 安全架构、威胁模型、命令安全、凭据处理 | [Security Whitepaper](SECURITY.md) |
| [数据保护承诺](DATA_PROTECTION.zh-CN.md) | 数据最小化、存储位置、用户权利、数据出境 | [Data Protection](DATA_PROTECTION.md) |
| [合规与责任声明](COMPLIANCE.zh-CN.md) | 法律框架对齐、责任边界、真实声明 | [Compliance](COMPLIANCE.md) |

### L0 · 治理 Governance

| 文档 | 内容 | English |
|---|---|---|
| [治理章程](governance/GOVERNANCE.zh-CN.md) | 治理框架、政策层级、角色职责(RACI)、审查周期、指标 | [Governance Charter](governance/GOVERNANCE.md) |

### L1 · 政策 Policies

| 文档 | 内容 | English |
|---|---|---|
| [信息安全总政策](policies/INFORMATION_SECURITY_POLICY.zh-CN.md) | CIA 三元组、控制域、访问与数据保护原则 | [Information Security Policy](policies/INFORMATION_SECURITY_POLICY.md) |
| [数据分级分类政策](policies/DATA_CLASSIFICATION.zh-CN.md) | 数据分级、处理位置、生命周期 | [Data Classification](policies/DATA_CLASSIFICATION.md) |
| [访问控制政策](policies/ACCESS_CONTROL.zh-CN.md) | 权限模式、命令执行控制、审计 | [Access Control](policies/ACCESS_CONTROL.md) |
| [AI 治理政策](policies/AI_GOVERNANCE.zh-CN.md) | 负责任 AI、人在环中、输出安全 | [AI Governance](policies/AI_GOVERNANCE.md) |
| [事件响应政策](policies/INCIDENT_RESPONSE.zh-CN.md) | 事件分级、响应 SLA、通知义务 | [Incident Response Policy](policies/INCIDENT_RESPONSE.md) |
| [第三方风险政策](policies/THIRD_PARTY_RISK.zh-CN.md) | BYOK/MCP/插件、供应链控制 | [Third-Party Risk](policies/THIRD_PARTY_RISK.md) |
| [业务连续性政策](policies/BUSINESS_CONTINUITY.zh-CN.md) | 可用性目标、灾难场景、备份 | [Business Continuity](policies/BUSINESS_CONTINUITY.md) |

### L2 · 标准 Standards

| 文档 | 内容 | English |
|---|---|---|
| [密码学标准](standards/CRYPTOGRAPHY.zh-CN.md) | 传输/存储安全、哈希校验、密钥 | [Cryptography Standard](standards/CRYPTOGRAPHY.md) |
| [认证标准](standards/AUTHENTICATION.zh-CN.md) | 认证路径、凭据管理、OAuth | [Authentication Standard](standards/AUTHENTICATION.md) |
| [日志与监控标准](standards/LOGGING_MONITORING.zh-CN.md) | 审计日志、脱敏、监控 | [Logging & Monitoring](standards/LOGGING_MONITORING.md) |
| [安全开发标准](standards/SECURE_DEVELOPMENT.zh-CN.md) | SDLC、命令安全、AI 安全 | [Secure Development](standards/SECURE_DEVELOPMENT.md) |

### L3 · 流程 Procedures

| 文档 | 内容 | English |
|---|---|---|
| [事件响应操作手册](procedures/INCIDENT_RESPONSE_RUNBOOK.zh-CN.md) | 分步响应、遏制、复盘 | [Incident Response Runbook](procedures/INCIDENT_RESPONSE_RUNBOOK.md) |
| [漏洞披露流程](procedures/VULNERABILITY_DISCLOSURE.zh-CN.md) | CVD、悬赏、报告处理 | [Vulnerability Disclosure](procedures/VULNERABILITY_DISCLOSURE.md) |
| [数据主体请求流程](procedures/DATA_SUBJECT_REQUEST.zh-CN.md) | 访问/删除/撤回等权利处理 | [DSR Handling](procedures/DATA_SUBJECT_REQUEST.md) |
| [备份与恢复流程](procedures/BACKUP_RECOVERY.zh-CN.md) | 备份、恢复、单会话恢复 | [Backup & Recovery](procedures/BACKUP_RECOVERY.md) |

### L4 · 合规 Compliance

| 文档 | 内容 | English |
|---|---|---|
| [全球合规对照矩阵](compliance/COMPLIANCE_MATRIX.zh-CN.md) | GDPR/PIPL/CCPA/LGPD 等原则对照 | [Compliance Matrix](compliance/COMPLIANCE_MATRIX.md) |
| [隐私影响评估 DPIA](compliance/DPIA.zh-CN.md) | 评估方法与风险缓解 | [DPIA](compliance/DPIA.md) |
| [数据处理活动记录 ROPA](compliance/ROPA.zh-CN.md) | 处理活动清单、接收方、保留期 | [ROPA](compliance/ROPA.md) |
| [数据传输影响评估 TIA](compliance/TRANSFER_ASSESSMENT.zh-CN.md) | 跨境传输分析与保护 | [TIA](compliance/TRANSFER_ASSESSMENT.md) |

### L5 · 信任 Trust

| 文档 | 内容 | English |
|---|---|---|
| [信任中心](trust/TRUST_CENTER.zh-CN.md) | 可信披露入口、事实速览 | [Trust Center](trust/TRUST_CENTER.md) |
| [次级处理者清单](trust/SUBPROCESSORS.zh-CN.md) | 第三方处理者披露 | [Subprocessors](trust/SUBPROCESSORS.md) |
| [透明度报告](trust/TRANSPARENCY_REPORT.zh-CN.md) | 收集概览、政府请求、事件 | [Transparency Report](trust/TRANSPARENCY_REPORT.md) |

---

## 适用范围

本体系适用于 FuXi 官方发布的二进制（通过 https://downloads.fuxicode.com 安装或以其他官方渠道分发）。

以下场景的隐私保护由**相应第三方**负责，我们已在文档中如实说明，请参阅：

- 你通过 **自带密钥** 使用的模型提供商（其各自的隐私政策与数据处理条款适用）；
- 你通过 **MCP** 接入的第三方服务器；
- 你安装的 **hooks / skills / plugins**（请仅从可信来源安装，并审阅其行为）。

---

## 我们的核心承诺（摘要）

1. **默认本地**：不强制注册/登录，数据默认留在你的设备。
2. **最小化收集**：仅处理为运行产品所必需的最少量数据。
3. **透明**：数据流向如实披露，不隐藏任何遥测或后台上传。
4. **由你掌控**：提供清晰的权限模型、审计日志与删除方式。
5. **真实**：不虚构认证，不夸大承诺；做不到的不说。
6. **完整**：治理→政策→标准→流程→合规→信任 六层覆盖。

---

## 重要说明：关于"最安全"

本体系以**对标全球最高标准、业界最完整**为目标设计与维护。我们如实披露
能力与边界，**不声称**任何未经客观验证的绝对化结论（如"全球最安全认证"）。
安全的可信度，来自可验证的架构与透明的披露，而非口号。

---

*最后更新：2026-08-23 · 版本 1.1 · 主体：FUXI*
