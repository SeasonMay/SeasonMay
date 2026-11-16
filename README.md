<p align="center">
  <img src="./assets/header.svg" alt="SeasonMay — Build. Verify. Improve." width="100%" />
</p>

<p align="center">
  <b>你好，我是 SeasonMay。</b><br />
  探索 AI 应用与系统工程，在开源实践中理解问题、验证修复。
</p>

<p align="center">
  <a href="https://github.com/SeasonMay?tab=repositories">项目仓库</a> ·
  <a href="https://github.com/pulls?q=is%3Apr+author%3ASeasonMay">开源贡献</a> ·
  <a href="https://github.com/SeasonMay?tab=stars">关注的项目</a>
</p>

---

### 最近在做

- **AI 应用与数据**：阅读 HugeGraph AI / Ontogeny，关注文档处理与业务模型。
- **工程可靠性**：从事件通知、路径校验和过滤规则等具体问题入手，补充可复现的回归测试。
- **动手验证**：用 Python、pytest 和 Docker 对比修复前后的实际行为。

### 开源实践

围绕 [HugeGraph AI](https://github.com/hugegraph/hugegraph-ai) 的问题复现、修复与测试。以下是提交的 PR；是否合并以各 PR 页面为准。

| 方向 | 改进 | 链接 |
| :--- | :--- | :--- |
| 事件通知 | SSE 队列溢出时发送重新同步提示，隔离慢订阅者 | [#117](https://github.com/hugegraph/hugegraph-ai/pull/117) |
| 路径校验 | 按真实路径包含关系检查提示词文件的目录边界 | [#118](https://github.com/hugegraph/hugegraph-ai/pull/118) |
| 数据一致性 | 使用 corpus 根目录匹配文档过滤规则，保留文档身份 | [#119](https://github.com/hugegraph/hugegraph-ai/pull/119) |

<details>
<summary>更多文档扫描修复</summary>

- [#104](https://github.com/hugegraph/hugegraph-ai/pull/104)：glob 文件选择器遵守 Store 的 include/exclude。
- [#106](https://github.com/hugegraph/hugegraph-ai/pull/106)：指定单文件时，仅扫描目标文件。

</details>

### 探索中的方向

| 方向 | 仓库入口 |
| :--- | :--- |
| 微服务项目 | [SafeMicroService](https://github.com/SeasonMay/SafeMicroService) |
| 端侧 AI | [RK3588 Stable Diffusion](https://github.com/SeasonMay/RK3588-stable-diffusion-GPU) · Fork |
| 本地知识库 | [deepmemo](https://github.com/SeasonMay/deepmemo) · Fork |

<sub>Fork 项目保留上游作者归属；贡献细节以提交记录为准。</sub>

---

<p align="center"><sub>先把问题复现，再把改进验证清楚。</sub></p>
