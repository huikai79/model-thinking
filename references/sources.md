# 來源與逐項取捨紀錄

審查日期：2026-09-05。範圍為舊版十個領域檔中的全部 253 個編號條目、組合示例、入口及公開說明。全部做了內容與適用條件審查；**不代表 253 項都已完成原始研究查核或效果驗證**。來源狀態依下表區分全文、摘要、定位及未確認。保留既有 MIT 著作權聲明，移除公開安裝文的私人聯絡資訊與無實體資產連結。

## 分類與查核邊界

- **正式**：形式模型、演算法、數學性質或有明確定義的分析概念。成立須符合所列假設；放到真實場景仍需證據。
- **實證**：研究觀察到的現象／偏誤或效果命題，可能依任務、人群、量尺而變；標籤不代表普遍成立或本次已重做研究。
- **啟發法**：產生候選解釋、價值討論與操作提示，沒有正確性保證。歷史理論在本包只作啟發時亦歸此類。

原條目分類與新版卡片用途可能不同，例如形式化 bandit 被借用作職涯啟發。下方逐項表保留原概念性質；卡片標記的是本包實際提供的用途。多概念合併只是減少重複，並未將它們視為相同理論或獨立證據。

## 來源

<a id="editorial"></a>
### EDITORIAL

編輯性啟發與待驗提示。無普遍效力主張；本次未逐篇核對所有原始文獻。用途與限制為本包整理，不能把名稱、名人歸屬或效果量當已驗證。

<a id="unverified"></a>
### UNVERIFIED

未確認／移除操作性內容。原來源或效果在本次未確認。保留舊名稱是為了回答指定教學與追蹤修訂，不代表推薦使用。

<a id="foundation"></a>
### FOUNDATION

形式定義與基礎概念。已逐項做概念／條件審查，但未逐條完成外部原典查核。正式標記描述其邏輯性質，不是對實際情境的驗證。用於高風險精確計算時仍須核對適用定理。

<a id="meadows"></a>
### MEADOWS

[Donella Meadows, Leverage Points](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/)。已讀作者全文；支持存量／流量、回饋與槓桿點限制。作者明示這不是找到槓桿點的保證配方。

<a id="ferguson"></a>
### FERGUSON

[Thomas Ferguson, Optimal Stopping and Applications](https://www.math.ucla.edu/~tom/Stopping/Contents.html)。核對作者教材章節位置：第 2 章 secretary problem、第 7 章 bandit；形式條件已審查，這次未逐式重證或實作求解。

<a id="boyd"></a>
### BOYD

[Boyd & Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)。核對作者公開教材中的 relaxation／Lagrangian dual 與最優化範圍。Simulated annealing 的特定收斂定理未另核對，本包不宣稱一般最優保證。

<a id="scheduling"></a>
### SCHEDULING

[Kleinberg–Tardos／Kevin Wayne, Greedy Algorithms](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/04GreedyAlgorithmsI.pdf)；[Hall et al., Scheduling to Minimize Average Completion Time](https://web.mit.edu/schulz/www/epapers/hssw-mor-1997.pdf)。核對 EDD 不要求工作等長；研究論文確認單機 Smith 按 p/w 非遞減排序。這不驗證產品開發 WSJF 的估計輸入。

<a id="nist"></a>
### NIST

[NIST, Confidence Limits for the Mean](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm)。已讀官方方法說明，核對重複區間程序的涵蓋率解釋。

<a id="isl"></a>
### ISL

[James et al., An Introduction to Statistical Learning](https://www.statlearning.com/)。核對作者教材入口與版本資訊；本次未逐章審查，僅作樣本外評估與過擬合的延伸閱讀，不宣稱引用頁面單獨支持全部細節。

<a id="powerlaw"></a>
### POWERLAW

[Clauset, Shalizi & Newman, Power-law distributions in empirical data](https://arxiv.org/abs/0706.1062)。核對原論文摘要及作者研究頁：分布需要估計、適合度檢驗與替代模型比較；領域名稱不保證冪次律。

<a id="hothand"></a>
### HOTHAND

[Miller & Sanjurjo, Surprised by the Hot Hand Fallacy?](https://arxiv.org/abs/1902.01265)。核對原研究摘要與出版紀錄；連勝條件式取樣的偏差可改變結論，不推定任一球員一定有 hot hand。

<a id="dunning"></a>
### DUNNING

[Kruger & Dunning (1999)](https://pubmed.ncbi.nlm.nih.gov/10626367/)；[Burson, Larrick & Klayman (2006)](https://doi.org/10.1037/0022-3514.90.1.60)。已讀原研究摘要；後者為對難度與相對自評的反證方向，本次由後續原研究引用定位，未通讀全文。刪除無來源的縱向山谷圖敘述，不宣稱效應已被完全推翻。

<a id="prospect"></a>
### PROSPECT

[Kahneman & Tversky, Prospect Theory (1979)](https://courses.washington.edu/pbafhall/514/514%20Readings/ProspectTheory.pdf)。核對原論文公開副本摘要／模型說明；參考點與風險態度不能簡化為人人固定兩倍損失。未為全部現狀偏誤逐篇查核。

<a id="bystander"></a>
### BYSTANDER

[Fischer et al. (2011), The bystander-effect](https://pubmed.ncbi.nlm.nih.gov/21534650/)。已讀研究綜合的摘要，危險與支援條件可能使效果減弱或非負；此來源是作者的綜合研究，非每項原始實驗重查。

<a id="lottery"></a>
### LOTTERY

[Lindqvist, Östling & Cesarini, Long-run Effects of Lottery Wealth](https://academic.oup.com/restud/article/87/6/2703/5734654)。核對原研究摘要與出版頁；彩票財富對生活滿意度的持續影響反對必回基準說法，不外推所有人或所有幸福指標。

<a id="maslow"></a>
### MASLOW

[Maslow (1943), A Theory of Human Motivation](https://psychclassics.yorku.ca/Maslow/motivation.htm)。來源定位但本次抓取逾時；沒有完成原文查核。因此只保留非階級強制的需求清單，歷史精確歸屬與普遍效度均待查。

<a id="network"></a>
### NETWORK

[Barabási, Network Science](https://networksciencebook.com/)。作者教材入口可開，但本次工具未擷取到章節內容；列為延伸原作者教材，圖論定義經編輯審查，不把分布與平台效應當本次已全文核證。

<a id="contagion"></a>
### CONTAGION

[Shalizi & Thomas, Homophily and Contagion Are Generically Confounded](https://arxiv.org/abs/1004.4704)。已讀原研究摘要，觀察網路中的同質性與傳染通常混淆；支持撤除肥胖等必然傳染的例子，不等於否認所有同伴效應。

<a id="dunbar"></a>
### DUNBAR

[Lindenfors et al. (2021), Dunbar’s number deconstructed](https://pmc.ncbi.nlm.nih.gov/articles/PMC8103230/)。核對原重分析的估計與寬區間；反對固定管理門檻，不主張關係維繫完全沒有認知限制。

<a id="porter"></a>
### PORTER

[Harvard Institute for Strategy and Competitiveness, The Five Forces](https://www.isc.hbs.edu/strategy/business-strategy/Pages/the-five-forces.aspx)。核對作者所屬研究單位的五力定義；將框架用途與企業獲利驗證分開。

<a id="disruption"></a>
### DISRUPTION

[Christensen Institute, Disruptive Innovation Theory](https://www.christenseninstitute.org/theory/disruptive-innovation/)。核對官方理論說明的 low-end／new-market 條件；不是所有新技術取代舊技術都屬此類。

<a id="pon"></a>
### PON

[Harvard Program on Negotiation, Zone of Possible Agreement](https://www.pon.harvard.edu/tag/zone-of-possible-agreement/)。核對官方教學對 BATNA 與 ZOPA 的定義；不宣稱特定讓步、錨定一定成功。

<a id="spacing"></a>
### SPACING

[Cepeda et al. (2006), Distributed practice in verbal recall tasks](https://pubmed.ncbi.nlm.nih.gov/16719566/)。核對作者綜合研究摘要；時間間隔與保留期間交互影響。這是統合分析，不是所有教材與技能的直接試驗。

<a id="retrieval"></a>
### RETRIEVAL

[Roediger & Karpicke (2006), Test-enhanced learning](https://pubmed.ncbi.nlm.nih.gov/16507066/)。核對原實驗摘要；支持特定學習材料的延後保留，不外推所有任務或沒有回饋的失敗提取。

<a id="practice"></a>
### PRACTICE

[Ericsson et al. (1993), The Role of Deliberate Practice](https://blogs.ischool.berkeley.edu/i225s14/files/2014/04/Ericsson-1993-article.pdf)；[Macnamara & Maitra (2019), Revisiting Ericsson et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC6731745/)。核對原論文與重做研究的公開摘要／結果脈絡；保留定義與研究分歧，不保留一萬小時門檻。

<a id="mindset"></a>
### MINDSET

[Yeager et al. (2019), A national experiment](https://www.nature.com/articles/s41586-019-1466-y)。核對原研究的情境異質性；效果不能脫離學生與學校環境推廣。

<a id="micro"></a>
### MICRO

[MIT OpenCourseWare, Principles of Microeconomics](https://ocw.mit.edu/courses/14-01sc-principles-of-microeconomics-fall-2011/)。核對官方教材主題範圍；作為生產、需求、效率與契約概念的延伸閱讀。本次未逐講推導所有定理，具體政策和價格仍需當地資料。

<a id="ostrom"></a>
### OSTROM

[Elinor Ostrom, Nobel Prize Lecture (2009)](https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/lecture/)。核對作者演講及投影片對多中心共同治理的論述；反駁公地只有私有化／中央管制或必然耗竭的二分。

## 取捨

保留有可執行動作且能說清條件的內容；合併重複的探索、資料檢查與跨域類比。移除未核名人引言、替使用者補原因或性格的故事，以及任意投資比例、固定心理倍率與健康操作建議。模型名稱仍能由下表追到處理結果；原題目指定已移除規則時，應解釋限制，不悄悄照用。

五個舊組合情境全部重寫為已知資訊、候選觀點、成立条件與待查事項。刪除固定三模型組合矩陣與跨域即驗證規則。入口保留指定模型、教學與深入探索；沒有模型數量配額。外部研究若顯示其他任務的短提示有效，也不能作為本包效果的證據。

## 對照後的補正

初輪回答暴露出估計查核不對稱、未提供的成本與持續性被當事實、計算混用起算點，以及為比較模型而錯限機會成本的適用範圍。本次補上對稱檢查、分段時間計算、跨期替代策略與新假說不自動否定原案的規則；沿用既有概念定義，不宣稱新增研究證據或效果已改善。實際增益須由修訂後的回答另行評估。

## 未編號的輔助名稱

舊速查表與組合表另出現下列名稱，並非 253 個編號條目的額外獨立模型。本次一併處理：

| 舊名稱／位置 | 分類 | 處理與理由 |
|---|---|---|
| Escalation／systems 速查表 | 啟發法 | 合併至 [回饋與振盪](systems.md#card-5)；互相加碼是待驗回饋假說，不保證尋求共同利益就能解決。 |
| Success to Successful／systems 速查表 | 啟發法 | 合併至 [路徑依賴與適應](systems.md#card-15)；資源優勢可能自我強化，但平等機會不是所有情境的唯一處方。 |
| Eroding Goals／systems 速查表 | 啟發法 | 合併至 [系統基模](systems.md#card-19)；目標下降需檢查原因，不能一律要求維持原目標。 |
| Map vs Territory／入口與 combinations | 啟發法 | 合併至 [入口](../SKILL.md) 的成立條件與類比差異檢查；模型是選擇性描述，不是現實本身，不需另一個固定套用模型。 |
| Small Wins／learning 速查表 | 啟發法 | 合併至 [小型學習試驗](learning.md#card-16)；成果需回饋與可承受成本，不宣稱小勝必能提高動機。 |
| Metcalfe’s Law／公開說明 | 啟發法 | 移除宣傳名稱；沒有條目提供完整模型與證據，不能用可能配對數推定實際網路價值。 |

## 舊條目逐項對照

### decisions

| 舊編號與名稱 | 原概念分類 | 處理／理由 | 新版位置 |
|---|---|---|---|
| 1. Inversion (Jacobi) | 啟發法 | 合併反向探索，保留三種動作差異，刪除名人引言。 | [反向找失敗：Inversion、Pre-Mortem、Devil’s Advocate](decisions.md#card-1) |
| 6. Pre-Mortem (Klein) | 啟發法 | 合併反向探索，保留三種動作差異，刪除名人引言。 | [反向找失敗：Inversion、Pre-Mortem、Devil’s Advocate](decisions.md#card-1) |
| 13. Devil's Advocate | 啟發法 | 合併反向探索，保留三種動作差異，刪除名人引言。 | [反向找失敗：Inversion、Pre-Mortem、Devil’s Advocate](decisions.md#card-1) |
| 2. Second-Order Thinking | 啟發法 | 保留；將必然因果範例改為條件式。 | [二階思考 Second-Order Thinking](decisions.md#card-2) |
| 3. Probabilistic Thinking | 啟發法 | 保留；移除無依據的成功機率。 | [機率式思考 Probabilistic Thinking](decisions.md#card-3) |
| 4. Expected Value | 正式 | 保留；移除正 EV 一律反覆下注的指令。 | [期望值 Expected Value](decisions.md#card-4) |
| 5. Regret Minimization (Bezos) | 啟發法 | 合併時間視角，刪名人背書與固定年齡結論。 | [時間距離：Regret Minimization、10/10/10](decisions.md#card-5) |
| 24. 10/10/10 Rule (Welch) | 啟發法 | 合併時間視角，刪名人背書與固定年齡結論。 | [時間距離：Regret Minimization、10/10/10](decisions.md#card-5) |
| 7. Two-Way vs One-Way Door (Bezos) | 啟發法 | 合併彈性取捨；不預設應等或應快。 | [可逆性與選擇權 Two-Way Door、Option Value](decisions.md#card-7) |
| 22. Option Value | 正式 | 合併彈性取捨；不預設應等或應快。 | [可逆性與選擇權 Two-Way Door、Option Value](decisions.md#card-7) |
| 8. Circle of Competence | 啟發法 | 保留；移除名人選股故事。 | [能力圈 Circle of Competence](decisions.md#card-8) |
| 9. Occam's Razor | 啟發法 | 合併；修正簡單較真、錯誤多為偶然等無條件主張。 | [替代解釋 Occam’s Razor、Hanlon’s Razor](decisions.md#card-9) |
| 10. Hanlon's Razor | 啟發法 | 合併；修正簡單較真、錯誤多為偶然等無條件主張。 | [替代解釋 Occam’s Razor、Hanlon’s Razor](decisions.md#card-9) |
| 11. First Principles Thinking | 啟發法 | 合併推理檢查；移除無法反駁即非知識的斷言。 | [從基礎重建與反駁 First Principles、Falsifiability](decisions.md#card-11) |
| 12. Falsifiability (Popper) | 啟發法 | 合併推理檢查；移除無法反駁即非知識的斷言。 | [從基礎重建與反駁 First Principles、Falsifiability](decisions.md#card-11) |
| 14. Six Thinking Hats (De Bono) | 啟發法 | 保留為流程；刪除強制排序。 | [六頂思考帽 Six Thinking Hats](decisions.md#card-14) |
| 15. Opportunity Cost | 正式 | 合併重複，主定義在 economics.md。 | [機會成本與邊際判斷 Opportunity Cost、Marginal Thinking](decisions.md#card-15) |
| 16. Marginal Thinking | 正式 | 合併重複，主定義在 economics.md。 | [機會成本與邊際判斷 Opportunity Cost、Marginal Thinking](decisions.md#card-15) |
| 17. Sunk Cost Fallacy | 實證 | 保留；區分不可收回支出與仍有用資產。 | [沉沒成本 Sunk Cost Fallacy](decisions.md#card-17) |
| 18. Asymmetric Risk-Reward | 啟發法 | 保留；刪除小額創投必為好賭注的暗示。 | [不對稱損益 Asymmetric Risk-Reward](decisions.md#card-18) |
| 19. Satisficing vs Maximizing (Simon) | 啟發法 | 合併選擇程序；刪除固定招聘規則與預設權重。 | [停止搜尋與加權比較 Satisficing、Weighted Decision Matrix](decisions.md#card-19) |
| 23. Weighted Decision Matrix | 啟發法 | 合併選擇程序；刪除固定招聘規則與預設權重。 | [停止搜尋與加權比較 Satisficing、Weighted Decision Matrix](decisions.md#card-19) |
| 20. Temporal Discounting | 正式 | 合併；不把折現一律視為偏誤或要求移除退出選項。 | [跨期選擇與承諾 Temporal Discounting、Commitment Devices](decisions.md#card-20) |
| 21. Commitment Devices | 啟發法 | 合併；不把折現一律視為偏誤或要求移除退出選項。 | [跨期選擇與承諾 Temporal Discounting、Commitment Devices](decisions.md#card-20) |
| 25. WRAP Framework (Heath) | 啟發法 | 保留名稱與常見展開；標明未核原書。 | [WRAP](decisions.md#card-25) |

### systems

| 舊編號與名稱 | 原概念分類 | 處理／理由 | 新版位置 |
|---|---|---|---|
| 1. Stocks and Flows | 正式 | 保留；修正存量公式與存量必慢的敘述。 | [存量與流量 Stocks and Flows](systems.md#card-1) |
| 2. System Boundaries | 正式 | 合併結構定義，移除泛化。 | [邊界與層級 System Boundaries、Hierarchy](systems.md#card-2) |
| 3. Hierarchy and Subsystems | 正式 | 合併結構定義，移除泛化。 | [邊界與層級 System Boundaries、Hierarchy](systems.md#card-2) |
| 4. Resilience | 正式 | 保留，補測量對象。 | [韌性 Resilience](systems.md#card-4) |
| 5. Reinforcing Feedback Loops (Positive) | 正式 | 合併動力機制，刪必然成長／穩定／振盪。 | [回饋、延遲與振盪 Feedback、Delays、Oscillation](systems.md#card-5) |
| 6. Balancing Feedback Loops (Negative) | 正式 | 合併動力機制，刪必然成長／穩定／振盪。 | [回饋、延遲與振盪 Feedback、Delays、Oscillation](systems.md#card-5) |
| 7. Delays | 正式 | 合併動力機制，刪必然成長／穩定／振盪。 | [回饋、延遲與振盪 Feedback、Delays、Oscillation](systems.md#card-5) |
| 8. Dominance Shifting | 正式 | 合併動力機制，刪必然成長／穩定／振盪。 | [回饋、延遲與振盪 Feedback、Delays、Oscillation](systems.md#card-5) |
| 9. Oscillation | 正式 | 合併動力機制，刪必然成長／穩定／振盪。 | [回饋、延遲與振盪 Feedback、Delays、Oscillation](systems.md#card-5) |
| 10. Exponential Growth | 正式 | 保留公式與限制；刪戲劇性描述。 | [指數成長 Exponential Growth](systems.md#card-10) |
| 11. Emergence | 正式 | 合併複雜性辨識；刪水分子類比與不可預測斷言。 | [湧現與非線性 Emergence、Non-linearity](systems.md#card-11) |
| 12. Non-linearity | 正式 | 合併複雜性辨識；刪水分子類比與不可預測斷言。 | [湧現與非線性 Emergence、Non-linearity](systems.md#card-11) |
| 13. Chaos and Sensitivity | 正式 | 合併；保留形式概念，限制跨域外推。 | [混沌與吸引子 Chaos、Attractors](systems.md#card-13) |
| 14. Attractors | 正式 | 合併；保留形式概念，限制跨域外推。 | [混沌與吸引子 Chaos、Attractors](systems.md#card-13) |
| 15. Path Dependence | 正式 | 合併相鄰概念，保留差別，移除未核歷史故事。 | [路徑依賴、自組織與適應](systems.md#card-15) |
| 16. Self-Organization | 正式 | 合併相鄰概念，保留差別，移除未核歷史故事。 | [路徑依賴、自組織與適應](systems.md#card-15) |
| 17. Adaptive Systems | 正式 | 合併相鄰概念，保留差別，移除未核歷史故事。 | [路徑依賴、自組織與適應](systems.md#card-15) |
| 18. Leverage Points (Meadows) | 啟發法 | 保留啟發用途；修正排序的確定性與第 4 點。 | [槓桿點 Leverage Points](systems.md#card-18) |
| 19. Unintended Consequences | 啟發法 | 合併診斷提示，全部降為待驗假說。 | [系統基模：副作用、政策阻力、轉嫁負擔、失效修補、成長限制](systems.md#card-19) |
| 20. Policy Resistance | 啟發法 | 合併診斷提示，全部降為待驗假說。 | [系統基模：副作用、政策阻力、轉嫁負擔、失效修補、成長限制](systems.md#card-19) |
| 21. Shifting the Burden | 啟發法 | 合併診斷提示，全部降為待驗假說。 | [系統基模：副作用、政策阻力、轉嫁負擔、失效修補、成長限制](systems.md#card-19) |
| 22. Fixes That Fail | 啟發法 | 合併診斷提示，全部降為待驗假說。 | [系統基模：副作用、政策阻力、轉嫁負擔、失效修補、成長限制](systems.md#card-19) |
| 23. Limits to Growth | 啟發法 | 合併診斷提示，全部降為待驗假說。 | [系統基模：副作用、政策阻力、轉嫁負擔、失效修補、成長限制](systems.md#card-19) |
| 24. Tragedy of the Commons | 正式 | 合併至經濟主條目並補反證。 | [公地與治理 Tragedy of the Commons](systems.md#card-24) |

### statistics

| 舊編號與名稱 | 原概念分類 | 處理／理由 | 新版位置 |
|---|---|---|---|
| 1. Bayes' Theorem | 正式 | 合併機率基礎；修正罕見疾病陽性結論。 | [條件機率、基準率、Bayes 與獨立性](statistics.md#card-1) |
| 2. Base Rates | 正式 | 合併機率基礎；修正罕見疾病陽性結論。 | [條件機率、基準率、Bayes 與獨立性](statistics.md#card-1) |
| 3. Conditional Probability | 正式 | 合併機率基礎；修正罕見疾病陽性結論。 | [條件機率、基準率、Bayes 與獨立性](statistics.md#card-1) |
| 4. Independence | 正式 | 合併機率基礎；修正罕見疾病陽性結論。 | [條件機率、基準率、Bayes 與獨立性](statistics.md#card-1) |
| 5. Law of Large Numbers | 正式 | 合併；移除賭場總會贏、正 EV 必下注。 | [大數法則與期望值](statistics.md#card-5) |
| 6. Expected Value | 正式 | 合併；移除賭場總會贏、正 EV 必下注。 | [大數法則與期望值](statistics.md#card-5) |
| 7. Normal Distribution (Gaussian) | 正式 | 保留，移除領域直接等於分布。 | [常態分布 Normal Distribution](statistics.md#card-7) |
| 8. Power Laws (Pareto) | 正式 | 合併；修正平均與分布推定。 | [冪次律與厚尾 Power Laws、Fat Tails](statistics.md#card-8) |
| 9. Fat Tails | 正式 | 合併；修正平均與分布推定。 | [冪次律與厚尾 Power Laws、Fat Tails](statistics.md#card-8) |
| 10. Regression to the Mean | 正式 | 保留，刪必然運氣變差敘述。 | [均值回歸 Regression to the Mean](statistics.md#card-10) |
| 11. Simpson's Paradox | 正式 | 保留；去除隐藏變數必解釋一切。 | [辛普森悖論 Simpson’s Paradox](statistics.md#card-11) |
| 12. Survivorship Bias | 正式 | 合併；將舊建築故事改為取樣檢查。 | [倖存與選擇偏差 Survivorship、Selection Bias](statistics.md#card-12) |
| 16. Selection Bias | 正式 | 合併；將舊建築故事改為取樣檢查。 | [倖存與選擇偏差 Survivorship、Selection Bias](statistics.md#card-12) |
| 13. Signal vs Noise | 正式 | 合併預測檢查，修正全是雜訊則資料無用。 | [訊號、過擬合與樣本量](statistics.md#card-13) |
| 17. Overfitting | 正式 | 合併預測檢查，修正全是雜訊則資料無用。 | [訊號、過擬合與樣本量](statistics.md#card-13) |
| 18. Sample Size Effects | 正式 | 合併預測檢查，修正全是雜訊則資料無用。 | [訊號、過擬合與樣本量](statistics.md#card-13) |
| 14. Confidence Intervals | 正式 | 保留，補明確頻率學派解釋。 | [信賴區間 Confidence Intervals](statistics.md#card-14) |
| 15. Correlation vs Causation | 正式 | 保留；刪未核案例的因果判定。 | [相關與因果 Correlation vs Causation](statistics.md#card-15) |
| 19. Multiple Comparisons Problem | 正式 | 保留；補保守檢定的上界、等號條件與期望／機率區別。 | [多重比較 Multiple Comparisons](statistics.md#card-19) |
| 20. Gambler's Fallacy | 實證 | 合併比較，修正 hot hand 先判謬誤的標籤。 | [連勝與獨立試驗 Gambler’s Fallacy、Hot Hand](statistics.md#card-20) |
| 21. Hot Hand Fallacy | 實證 | 合併比較，修正 hot hand 先判謬誤的標籤。 | [連勝與獨立試驗 Gambler’s Fallacy、Hot Hand](statistics.md#card-20) |
| 22. Neglect of Probability | 實證 | 合併檢查清單，保留 conjunction 的數學條件。 | [機率判斷失誤與分母檢查](statistics.md#card-22) |
| 23. Conjunction Fallacy | 正式 | 合併檢查清單，保留 conjunction 的數學條件。 | [機率判斷失誤與分母檢查](statistics.md#card-22) |
| 24. Denominator Neglect | 實證 | 合併檢查清單，保留 conjunction 的數學條件。 | [機率判斷失誤與分母檢查](statistics.md#card-22) |
| 25. Availability Heuristic | 實證 | 合併檢查清單，保留 conjunction 的數學條件。 | [機率判斷失誤與分母檢查](statistics.md#card-22) |

### strategy

| 舊編號與名稱 | 原概念分類 | 處理／理由 | 新版位置 |
|---|---|---|---|
| 1. Nash Equilibrium | 正式 | 合併正式賽局，補結構、資訊、噪音及均衡非最佳。 | [賽局、均衡與重複互動](strategy.md#card-1) |
| 2. Prisoner's Dilemma | 正式 | 合併正式賽局，補結構、資訊、噪音及均衡非最佳。 | [賽局、均衡與重複互動](strategy.md#card-1) |
| 3. Zero-Sum vs Positive-Sum | 正式 | 合併正式賽局，補結構、資訊、噪音及均衡非最佳。 | [賽局、均衡與重複互動](strategy.md#card-1) |
| 4. Repeated Games | 正式 | 合併正式賽局，補結構、資訊、噪音及均衡非最佳。 | [賽局、均衡與重複互動](strategy.md#card-1) |
| 5. Tit-for-Tat | 正式 | 合併正式賽局，補結構、資訊、噪音及均衡非最佳。 | [賽局、均衡與重複互動](strategy.md#card-1) |
| 6. Chicken Game | 正式 | 合併正式賽局，補結構、資訊、噪音及均衡非最佳。 | [賽局、均衡與重複互動](strategy.md#card-1) |
| 7. Stag Hunt | 正式 | 合併正式賽局，補結構、資訊、噪音及均衡非最佳。 | [賽局、均衡與重複互動](strategy.md#card-1) |
| 8. Moats (Competitive Advantage) | 啟發法 | 合併；刪未核公司優勢敘述。 | [競爭優勢 Moats、Porter’s Five Forces](strategy.md#card-8) |
| 9. Porter's Five Forces | 啟發法 | 合併；刪未核公司優勢敘述。 | [競爭優勢 Moats、Porter’s Five Forces](strategy.md#card-8) |
| 10. Relative vs Absolute Advantage | 正式 | 更名明確化並合併至 economics.md。 | [比較優勢 Comparative Advantage](strategy.md#card-10) |
| 11. First-Mover vs Fast-Follower | 啟發法 | 合併路線假說，刪除 MySpace 是第一等故事。 | [競爭路線 First-Mover／Fast-Follower、Blue Ocean、Red Queen](strategy.md#card-11) |
| 12. Blue Ocean Strategy | 啟發法 | 合併路線假說，刪除 MySpace 是第一等故事。 | [競爭路線 First-Mover／Fast-Follower、Blue Ocean、Red Queen](strategy.md#card-11) |
| 14. Red Queen Effect | 啟發法 | 合併路線假說，刪除 MySpace 是第一等故事。 | [競爭路線 First-Mover／Fast-Follower、Blue Ocean、Red Queen](strategy.md#card-11) |
| 13. Disruptive Innovation (Christensen) | 啟發法 | 保留理論為假說框架；修正必然取代與在位者不能反應。 | [破壞式創新 Disruptive Innovation](strategy.md#card-13) |
| 15. BATNA (Best Alternative To Negotiated Agreement) | 啟發法 | 合併談判程序，刪預設底價。 | [談判替代方案 BATNA、ZOPA 與價值交換](strategy.md#card-15) |
| 16. ZOPA (Zone of Possible Agreement) | 啟發法 | 合併談判程序，刪預設底價。 | [談判替代方案 BATNA、ZOPA 與價值交換](strategy.md#card-15) |
| 17. Integrative vs Distributive Bargaining | 啟發法 | 合併談判程序，刪預設底價。 | [談判替代方案 BATNA、ZOPA 與價值交換](strategy.md#card-15) |
| 18. Anchoring in Negotiation | 實證 | 合併影響提示；移除強錨及製造義務的通用指令，效應待查。 | [錨定、承諾一致與互惠](strategy.md#card-18) |
| 19. Commitment and Consistency | 實證 | 合併影響提示；移除強錨及製造義務的通用指令，效應待查。 | [錨定、承諾一致與互惠](strategy.md#card-18) |
| 20. Reciprocity | 實證 | 合併影響提示；移除強錨及製造義務的通用指令，效應待查。 | [錨定、承諾一致與互惠](strategy.md#card-18) |
| 21. Schelling Points (Focal Points) | 正式 | 合併重複承諾與資訊概念，刪名人故事與成本即可信。 | [協調點、可信承諾、訊號與選擇權](strategy.md#card-21) |
| 22. Commitment Devices | 正式 | 合併重複承諾與資訊概念，刪名人故事與成本即可信。 | [協調點、可信承諾、訊號與選擇權](strategy.md#card-21) |
| 23. Signaling | 正式 | 合併重複承諾與資訊概念，刪名人故事與成本即可信。 | [協調點、可信承諾、訊號與選擇權](strategy.md#card-21) |
| 24. Information Asymmetry | 正式 | 合併重複承諾與資訊概念，刪名人故事與成本即可信。 | [協調點、可信承諾、訊號與選擇權](strategy.md#card-21) |
| 25. Option Value in Strategy | 正式 | 合併重複承諾與資訊概念，刪名人故事與成本即可信。 | [協調點、可信承諾、訊號與選擇權](strategy.md#card-21) |
| 26. Precommitment | 正式 | 合併重複承諾與資訊概念，刪名人故事與成本即可信。 | [協調點、可信承諾、訊號與選擇權](strategy.md#card-21) |

### psychology

| 舊編號與名稱 | 原概念分類 | 處理／理由 | 新版位置 |
|---|---|---|---|
| 1. Confirmation Bias | 實證 | 合併自我校正動作；本次未逐篇核對效應大小與復現。 | [自我檢查：確認、可得性、錨定、後見與過度自信](psychology.md#card-1) |
| 2. Availability Heuristic | 實證 | 合併自我校正動作；本次未逐篇核對效應大小與復現。 | [自我檢查：確認、可得性、錨定、後見與過度自信](psychology.md#card-1) |
| 3. Anchoring | 實證 | 合併自我校正動作；本次未逐篇核對效應大小與復現。 | [自我檢查：確認、可得性、錨定、後見與過度自信](psychology.md#card-1) |
| 4. Hindsight Bias | 實證 | 合併自我校正動作；本次未逐篇核對效應大小與復現。 | [自我檢查：確認、可得性、錨定、後見與過度自信](psychology.md#card-1) |
| 5. Overconfidence | 實證 | 合併自我校正動作；本次未逐篇核對效應大小與復現。 | [自我檢查：確認、可得性、錨定、後見與過度自信](psychology.md#card-1) |
| 6. Dunning-Kruger Effect | 實證 | 保留；刪流行曲線與專家必低估。 | [Dunning–Kruger Effect](psychology.md#card-6) |
| 7. Status Quo Bias | 實證 | 合併相鄰概念；刪固定倍率及一律解釋。 | [現狀、框架與損失 Status Quo、Framing、Loss Aversion](psychology.md#card-7) |
| 8. Framing Effects | 實證 | 合併相鄰概念；刪固定倍率及一律解釋。 | [現狀、框架與損失 Status Quo、Framing、Loss Aversion](psychology.md#card-7) |
| 9. Loss Aversion (Kahneman) | 實證 | 合併相鄰概念；刪固定倍率及一律解釋。 | [現狀、框架與損失 Status Quo、Framing、Loss Aversion](psychology.md#card-7) |
| 10. Peak-End Rule | 實證 | 合併；刪中間必被忘記及旅遊必以峰尾決定。 | [回憶與順序 Peak-End、Recency／Primacy](psychology.md#card-10) |
| 11. Recency and Primacy Effects | 實證 | 合併；刪中間必被忘記及旅遊必以峰尾決定。 | [回憶與順序 Peak-End、Recency／Primacy](psychology.md#card-10) |
| 12. Halo Effect | 實證 | 合併評估動作；修正不同歸因效應混同，實證適用性待查。 | [特質推斷與歸因 Halo、Attribution、Representativeness、Self-Serving](psychology.md#card-12) |
| 13. Fundamental Attribution Error | 實證 | 合併評估動作；修正不同歸因效應混同，實證適用性待查。 | [特質推斷與歸因 Halo、Attribution、Representativeness、Self-Serving](psychology.md#card-12) |
| 14. Representativeness Heuristic | 實證 | 合併評估動作；修正不同歸因效應混同，實證適用性待查。 | [特質推斷與歸因 Halo、Attribution、Representativeness、Self-Serving](psychology.md#card-12) |
| 26. Self-Serving Bias | 實證 | 合併評估動作；修正不同歸因效應混同，實證適用性待查。 | [特質推斷與歸因 Halo、Attribution、Representativeness、Self-Serving](psychology.md#card-12) |
| 15. Social Proof | 實證 | 合併為待驗線索；刪未核群體事件、推定職業動機與名人引言。 | [社會影響與動機假說](psychology.md#card-15) |
| 16. Authority Bias | 實證 | 合併為待驗線索；刪未核群體事件、推定職業動機與名人引言。 | [社會影響與動機假說](psychology.md#card-15) |
| 17. Liking Bias | 實證 | 合併為待驗線索；刪未核群體事件、推定職業動機與名人引言。 | [社會影響與動機假說](psychology.md#card-15) |
| 18. Commitment and Consistency (Cialdini) | 實證 | 合併為待驗線索；刪未核群體事件、推定職業動機與名人引言。 | [社會影響與動機假說](psychology.md#card-15) |
| 19. In-Group/Out-Group Bias | 實證 | 合併為待驗線索；刪未核群體事件、推定職業動機與名人引言。 | [社會影響與動機假說](psychology.md#card-15) |
| 20. Groupthink | 實證 | 合併為待驗線索；刪未核群體事件、推定職業動機與名人引言。 | [社會影響與動機假說](psychology.md#card-15) |
| 22. Incentive-Caused Bias | 實證 | 合併為待驗線索；刪未核群體事件、推定職業動機與名人引言。 | [社會影響與動機假說](psychology.md#card-15) |
| 23. Reactance | 實證 | 合併為待驗線索；刪未核群體事件、推定職業動機與名人引言。 | [社會影響與動機假說](psychology.md#card-15) |
| 21. Bystander Effect | 實證 | 保留動作，補可信反證與情境限制。 | [旁觀者效應 Bystander Effect](psychology.md#card-21) |
| 24. Hedonic Treadmill | 實證 | 保留適應問題；刪彩票贏家必回基準。 | [享樂適應 Hedonic Adaptation](psychology.md#card-24) |
| 25. Maslow's Hierarchy | 啟發法 | 降為需求清單；移除階層必然性並揭露來源限制。 | [Maslow’s Hierarchy](psychology.md#card-25) |
| 27. Sunk Cost Fallacy | 實證 | 合併至 decisions.md 主條目。 | [Sunk Cost Fallacy](psychology.md#card-27) |

### networks

| 舊編號與名稱 | 原概念分類 | 處理／理由 | 新版位置 |
|---|---|---|---|
| 1. Nodes and Edges | 正式 | 合併結構定義，刪無條件傳播與分布推定。 | [網路結構：Nodes、Edges、Density、Degree、Hubs、Clustering](networks.md#card-1) |
| 2. Network Density | 正式 | 合併結構定義，刪無條件傳播與分布推定。 | [網路結構：Nodes、Edges、Density、Degree、Hubs、Clustering](networks.md#card-1) |
| 3. Degree Distribution | 正式 | 合併結構定義，刪無條件傳播與分布推定。 | [網路結構：Nodes、Edges、Density、Degree、Hubs、Clustering](networks.md#card-1) |
| 4. Hub Nodes | 正式 | 合併結構定義，刪無條件傳播與分布推定。 | [網路結構：Nodes、Edges、Density、Degree、Hubs、Clustering](networks.md#card-1) |
| 5. Network Clustering | 正式 | 合併結構定義，刪無條件傳播與分布推定。 | [網路結構：Nodes、Edges、Density、Degree、Hubs、Clustering](networks.md#card-1) |
| 6. Bridges and Structural Holes (Burt) | 實證 | 合併連結用途；本次未逐篇驗證原始經驗研究。 | [橋接、結構洞與弱連結](networks.md#card-6) |
| 7. Strong vs Weak Ties (Granovetter) | 實證 | 合併連結用途；本次未逐篇驗證原始經驗研究。 | [橋接、結構洞與弱連結](networks.md#card-6) |
| 8. Small World Networks | 正式 | 合併生成模型，補假設。 | [Small World、Preferential Attachment](networks.md#card-8) |
| 9. Preferential Attachment (Barabási) | 正式 | 合併生成模型，補假設。 | [Small World、Preferential Attachment](networks.md#card-8) |
| 10. Network Effects | 正式 | 合併平台機制，移除 winner-take-all 必然性。 | [Network Effects、Critical Mass 與平台](networks.md#card-10) |
| 11. Critical Mass | 正式 | 合併平台機制，移除 winner-take-all 必然性。 | [Network Effects、Critical Mass 與平台](networks.md#card-10) |
| 12. Tipping Points | 正式 | 合併平台機制，移除 winner-take-all 必然性。 | [Network Effects、Critical Mass 與平台](networks.md#card-10) |
| 20. Two-Sided Markets | 正式 | 合併平台機制，移除 winner-take-all 必然性。 | [Network Effects、Critical Mass 與平台](networks.md#card-10) |
| 21. Multi-Sided Platforms | 正式 | 合併平台機制，移除 winner-take-all 必然性。 | [Network Effects、Critical Mass 與平台](networks.md#card-10) |
| 13. Cascade Failures | 正式 | 合併傳播模型但保留機制差異，修正密度及 R 定義。 | [連鎖失效與擴散 Cascade Failures、Viral Spread](networks.md#card-13) |
| 16. Viral Spread | 正式 | 合併傳播模型但保留機制差異，修正密度及 R 定義。 | [連鎖失效與擴散 Cascade Failures、Viral Spread](networks.md#card-13) |
| 14. Social Contagion | 實證 | 合併辨識問題，刪相關即傳染的例子。 | [社會傳染、資訊瀑布與同溫層](networks.md#card-14) |
| 15. Information Cascade | 正式 | 合併辨識問題，刪相關即傳染的例子。 | [社會傳染、資訊瀑布與同溫層](networks.md#card-14) |
| 18. Echo Chambers | 實證 | 合併辨識問題，刪相關即傳染的例子。 | [社會傳染、資訊瀑布與同溫層](networks.md#card-14) |
| 17. Seeding Strategies | 啟發法 | 合併策略啟發，不以平台故事作證。 | [播種與生態系 Seeding、Network Orchestration、Ecosystem Strategy](networks.md#card-17) |
| 24. Network Orchestration | 啟發法 | 合併策略啟發，不以平台故事作證。 | [播種與生態系 Seeding、Network Orchestration、Ecosystem Strategy](networks.md#card-17) |
| 25. Ecosystem Strategy | 啟發法 | 合併策略啟發，不以平台故事作證。 | [播種與生態系 Seeding、Network Orchestration、Ecosystem Strategy](networks.md#card-17) |
| 19. Dunbar's Number | 實證 | 保留爭議名稱供教學，移除人數階層與治理門檻。 | [Dunbar’s Number](networks.md#card-19) |
| 22. Switching Costs and Lock-In | 正式 | 合併交易結構，去除必然優勢。 | [轉換成本與去中介 Switching Costs、Disintermediation](networks.md#card-22) |
| 23. Disintermediation | 啟發法 | 合併交易結構，去除必然優勢。 | [轉換成本與去中介 Switching Costs、Disintermediation](networks.md#card-22) |

### algorithms

| 舊編號與名稱 | 原概念分類 | 處理／理由 | 新版位置 |
|---|---|---|---|
| 1. Optimal Stopping (37% Rule) | 正式 | 合併停止問題與變體，補全部核心假設。 | [最佳停止 Optimal Stopping／Secretary Problem](algorithms.md#card-1) |
| 2. Look-Then-Leap Rule | 正式 | 合併停止問題與變體，補全部核心假設。 | [最佳停止 Optimal Stopping／Secretary Problem](algorithms.md#card-1) |
| 3. Secretary Problem Variants | 正式 | 合併停止問題與變體，補全部核心假設。 | [最佳停止 Optimal Stopping／Secretary Problem](algorithms.md#card-1) |
| 4. Multi-Armed Bandit | 正式 | 合併探索概念，修正 Gittins 比喻與年齡規則。 | [Bandit、Explore／Exploit、Gittins Index](algorithms.md#card-4) |
| 5. Explore/Exploit Trade-off | 正式 | 合併探索概念，修正 Gittins 比喻與年齡規則。 | [Bandit、Explore／Exploit、Gittins Index](algorithms.md#card-4) |
| 6. Gittins Index | 正式 | 合併探索概念，修正 Gittins 比喻與年齡規則。 | [Bandit、Explore／Exploit、Gittins Index](algorithms.md#card-4) |
| 7. Comparison Sorts | 正式 | 合併排序；區分類比與演算法保證。 | [Comparison Sorts、Bucket Sort](algorithms.md#card-7) |
| 8. Bucket Sort | 正式 | 合併排序；區分類比與演算法保證。 | [Comparison Sorts、Bucket Sort](algorithms.md#card-7) |
| 9. Search Costs | 正式 | 合併整理類比，LRU 技術定義保留；移除必然高效。 | [Search Costs、LRU、Noguchi Filing](algorithms.md#card-9) |
| 10. LRU Cache (Least Recently Used) | 正式 | 合併整理類比，LRU 技術定義保留；移除必然高效。 | [Search Costs、LRU、Noguchi Filing](algorithms.md#card-9) |
| 11. The Noguchi Filing System | 啟發法 | 合併整理類比，LRU 技術定義保留；移除必然高效。 | [Search Costs、LRU、Noguchi Filing](algorithms.md#card-9) |
| 12. Earliest Due Date | 正式 | 合併排程，修正 EDD 同長限制及加權規則。 | [排程 EDD、SJF、Weighted SJF](algorithms.md#card-12) |
| 13. Shortest Job First | 正式 | 合併排程，修正 EDD 同長限制及加權規則。 | [排程 EDD、SJF、Weighted SJF](algorithms.md#card-12) |
| 14. Weighted Shortest Job First | 正式 | 合併排程，修正 EDD 同長限制及加權規則。 | [排程 EDD、SJF、Weighted SJF](algorithms.md#card-12) |
| 15. Priority Inversion | 正式 | 合併資源管理，移除一般會議即優先反轉的例子。 | [阻塞、批次與切換 Priority Inversion、Coalescing、Thrashing](algorithms.md#card-15) |
| 16. Interrupt Coalescing | 正式 | 合併資源管理，移除一般會議即優先反轉的例子。 | [阻塞、批次與切換 Priority Inversion、Coalescing、Thrashing](algorithms.md#card-15) |
| 17. Context Switching Costs | 實證 | 合併資源管理，移除一般會議即優先反轉的例子。 | [阻塞、批次與切換 Priority Inversion、Coalescing、Thrashing](algorithms.md#card-15) |
| 18. Thrashing | 正式 | 合併資源管理，移除一般會議即優先反轉的例子。 | [阻塞、批次與切換 Priority Inversion、Coalescing、Thrashing](algorithms.md#card-15) |
| 19. Gradient Descent | 正式 | 合併最佳化方法，補條件；annealing 機率規格本次未另推導。 | [Gradient Descent、Hill Climbing、Simulated Annealing、Random Restarts](algorithms.md#card-19) |
| 20. Simulated Annealing | 正式 | 合併最佳化方法，補條件；annealing 機率規格本次未另推導。 | [Gradient Descent、Hill Climbing、Simulated Annealing、Random Restarts](algorithms.md#card-19) |
| 21. Hill Climbing | 正式 | 合併最佳化方法，補條件；annealing 機率規格本次未另推導。 | [Gradient Descent、Hill Climbing、Simulated Annealing、Random Restarts](algorithms.md#card-19) |
| 22. Randomness in Optimization | 正式 | 合併最佳化方法，補條件；annealing 機率規格本次未另推導。 | [Gradient Descent、Hill Climbing、Simulated Annealing、Random Restarts](algorithms.md#card-19) |
| 23. Relaxation | 正式 | 合併；修正把硬限制一律變柔性成本。 | [約束與鬆弛 Constraint Satisfaction、Relaxation、Lagrangian Relaxation](algorithms.md#card-23) |
| 24. Constraint Satisfaction | 正式 | 合併；修正把硬限制一律變柔性成本。 | [約束與鬆弛 Constraint Satisfaction、Relaxation、Lagrangian Relaxation](algorithms.md#card-23) |
| 25. Lagrangian Relaxation | 正式 | 合併；修正把硬限制一律變柔性成本。 | [約束與鬆弛 Constraint Satisfaction、Relaxation、Lagrangian Relaxation](algorithms.md#card-23) |

### risk

| 舊編號與名稱 | 原概念分類 | 處理／理由 | 新版位置 |
|---|---|---|---|
| 1. Risk vs Uncertainty (Knight) | 啟發法 | 合併分類；刪保險已知、創業未知及寬區間即校準。 | [不確定性與校準](risk.md#card-1) |
| 2. Aleatory vs Epistemic Uncertainty | 正式 | 合併分類；刪保險已知、創業未知及寬區間即校準。 | [不確定性與校準](risk.md#card-1) |
| 3. Known Knowns Matrix (Rumsfeld) | 啟發法 | 合併分類；刪保險已知、創業未知及寬區間即校準。 | [不確定性與校準](risk.md#card-1) |
| 4. Calibrated Uncertainty | 正式 | 合併分類；刪保險已知、創業未知及寬區間即校準。 | [不確定性與校準](risk.md#card-1) |
| 5. Ergodicity | 正式 | 保留正式概念；移除未定義群體平均的例子。 | [Ergodicity](risk.md#card-5) |
| 6. Fragile | 啟發法 | 合併脆弱性分析；刪運動、免疫等醫療外推。 | [Fragile、Robust、Antifragile、Via Negativa](risk.md#card-6) |
| 7. Robust | 啟發法 | 合併脆弱性分析；刪運動、免疫等醫療外推。 | [Fragile、Robust、Antifragile、Via Negativa](risk.md#card-6) |
| 8. Antifragile (Taleb) | 啟發法 | 合併脆弱性分析；刪運動、免疫等醫療外推。 | [Fragile、Robust、Antifragile、Via Negativa](risk.md#card-6) |
| 10. Via Negativa | 啟發法 | 合併脆弱性分析；刪運動、免疫等醫療外推。 | [Fragile、Robust、Antifragile、Via Negativa](risk.md#card-6) |
| 9. Hormesis | 實證 | 移除操作性內容及醫療例子；保留名稱與移除理由。 | [Hormesis：僅供辨識的已移除建議](risk.md#card-9) |
| 11. Black Swans | 啟發法 | 合併尾部提醒，移除 COVID 等事件標籤及平均一律無意義。 | [尾風險與模型外事件](risk.md#card-11) |
| 12. Fat Tails vs Thin Tails | 正式 | 合併尾部提醒，移除 COVID 等事件標籤及平均一律無意義。 | [尾風險與模型外事件](risk.md#card-11) |
| 13. Ludic Fallacy | 啟發法 | 合併尾部提醒，移除 COVID 等事件標籤及平均一律無意義。 | [尾風險與模型外事件](risk.md#card-11) |
| 14. Turkey Problem | 啟發法 | 合併尾部提醒，移除 COVID 等事件標籤及平均一律無意義。 | [尾風險與模型外事件](risk.md#card-11) |
| 15. Extremistan vs Mediocristan | 啟發法 | 合併尾部提醒，移除 COVID 等事件標籤及平均一律無意義。 | [尾風險與模型外事件](risk.md#card-11) |
| 16. Precautionary Principle | 啟發法 | 合併防護動作，刪特定政治科技斷言與任意工程係數。 | [預防、緩衝與備援](risk.md#card-16) |
| 17. Margin of Safety | 啟發法 | 合併防護動作，刪特定政治科技斷言與任意工程係數。 | [預防、緩衝與備援](risk.md#card-16) |
| 19. Redundancy | 啟發法 | 合併防護動作，刪特定政治科技斷言與任意工程係數。 | [預防、緩衝與備援](risk.md#card-16) |
| 18. Barbell Strategy | 啟發法 | 合併風險配置，移除金融比例、錯誤 Kelly 公式與必然小賭注優勢。 | [曝險、選擇權與小型實驗](risk.md#card-18) |
| 20. Position Sizing | 正式 | 合併風險配置，移除金融比例、錯誤 Kelly 公式與必然小賭注優勢。 | [曝險、選擇權與小型實驗](risk.md#card-18) |
| 21. Asymmetric Payoffs | 正式 | 合併風險配置，移除金融比例、錯誤 Kelly 公式與必然小賭注優勢。 | [曝險、選擇權與小型實驗](risk.md#card-18) |
| 23. Small Bets | 啟發法 | 合併風險配置，移除金融比例、錯誤 Kelly 公式與必然小賭注優勢。 | [曝險、選擇權與小型實驗](risk.md#card-18) |
| 24. Reversibility Premium | 啟發法 | 合併風險配置，移除金融比例、錯誤 Kelly 公式與必然小賭注優勢。 | [曝險、選擇權與小型實驗](risk.md#card-18) |
| 22. Skin in the Game | 啟發法 | 合併壓力檢查，移除職業倫理比喻與全部資產同跌。 | [誘因一致與壓力依存性](risk.md#card-22) |
| 25. Correlation in Crisis | 實證 | 合併壓力檢查，移除職業倫理比喻與全部資產同跌。 | [誘因一致與壓力依存性](risk.md#card-22) |

### learning

| 舊編號與名稱 | 原概念分類 | 處理／理由 | 新版位置 |
|---|---|---|---|
| 1. Circle of Competence | 啟發法 | 合併知識範圍，能力圈與決策主條目一致。 | [能力圈與 T-Shaped Knowledge](learning.md#card-1) |
| 2. T-Shaped Knowledge | 啟發法 | 合併知識範圍，能力圈與決策主條目一致。 | [能力圈與 T-Shaped Knowledge](learning.md#card-1) |
| 3. Spacing Effect | 實證 | 合併練習安排，修正固定間隔與痛苦即有效。 | [Spacing Effect、Testing Effect](learning.md#card-3) |
| 4. Testing Effect | 實證 | 合併練習安排，修正固定間隔與痛苦即有效。 | [Spacing Effect、Testing Effect](learning.md#card-3) |
| 5. Interleaving | 實證 | 合併教學候選策略，不宣稱詞圖或交錯必勝。 | [Interleaving、Elaboration、Dual Coding、Desirable Difficulties](learning.md#card-5) |
| 6. Elaboration | 實證 | 合併教學候選策略，不宣稱詞圖或交錯必勝。 | [Interleaving、Elaboration、Dual Coding、Desirable Difficulties](learning.md#card-5) |
| 7. Dual Coding | 實證 | 合併教學候選策略，不宣稱詞圖或交錯必勝。 | [Interleaving、Elaboration、Dual Coding、Desirable Difficulties](learning.md#card-5) |
| 15. Desirable Difficulties | 實證 | 合併教學候選策略，不宣稱詞圖或交錯必勝。 | [Interleaving、Elaboration、Dual Coding、Desirable Difficulties](learning.md#card-5) |
| 8. Deliberate Practice (Ericsson) | 實證 | 合併；移除固定時數與停滯單因果。 | [Deliberate Practice、練習時數與 Plateau](learning.md#card-8) |
| 9. 10,000 Hour Rule (Modified) | 實證 | 合併；移除固定時數與停滯單因果。 | [Deliberate Practice、練習時數與 Plateau](learning.md#card-8) |
| 11. Plateau Effect | 實證 | 合併；移除固定時數與停滯單因果。 | [Deliberate Practice、練習時數與 Plateau](learning.md#card-8) |
| 10. Competence Ladder | 啟發法 | 保留名稱供教學；移除必然階梯與懸念示例。 | [Competence Ladder、Zeigarnik Effect：降為待查提示](learning.md#card-10) |
| 13. Zeigarnik Effect | 實證 | 保留名稱供教學；移除必然階梯與懸念示例。 | [Competence Ladder、Zeigarnik Effect：降為待查提示](learning.md#card-10) |
| 12. Transfer of Learning | 實證 | 合併跨域學習，刪知識必指數增長與職涯年齡規則。 | [遷移、類比與探索](learning.md#card-12) |
| 18. Explore/Exploit Trade-off | 正式 | 合併跨域學習，刪知識必指數增長與職涯年齡規則。 | [遷移、類比與探索](learning.md#card-12) |
| 19. Compounding Knowledge | 啟發法 | 合併跨域學習，刪知識必指數增長與職涯年齡規則。 | [遷移、類比與探索](learning.md#card-12) |
| 21. Analogical Reasoning | 實證 | 合併跨域學習，刪知識必指數增長與職涯年齡規則。 | [遷移、類比與探索](learning.md#card-12) |
| 14. Growth vs Fixed Mindset (Dweck) | 實證 | 保留，補原研究情境限制。 | [Growth Mindset](learning.md#card-14) |
| 16. Fail Fast, Learn Fast | 啟發法 | 合併試驗啟發，刪快迭代普遍勝規劃與肌肉類比。 | [Fail Fast、Antifragility in Learning](learning.md#card-16) |
| 17. Antifragility in Learning | 啟發法 | 合併試驗啟發，刪快迭代普遍勝規劃與肌肉類比。 | [Fail Fast、Antifragility in Learning](learning.md#card-16) |
| 20. Feynman Technique | 啟發法 | 保留用途；刪未核名人引言。 | [Feynman Technique](learning.md#card-20) |
| 22. Scaffolding | 啟發法 | 合併教學設計，修正 ZPD 定義與固定容量。 | [支架、認知負荷、ZPD 與 Chunking](learning.md#card-22) |
| 23. Cognitive Load Theory | 正式 | 合併教學設計，修正 ZPD 定義與固定容量。 | [支架、認知負荷、ZPD 與 Chunking](learning.md#card-22) |
| 24. Zone of Proximal Development (Vygotsky) | 正式 | 合併教學設計，修正 ZPD 定義與固定容量。 | [支架、認知負荷、ZPD 與 Chunking](learning.md#card-22) |
| 25. Chunking | 正式 | 合併教學設計，修正 ZPD 定義與固定容量。 | [支架、認知負荷、ZPD 與 Chunking](learning.md#card-22) |

### economics

| 舊編號與名稱 | 原概念分類 | 處理／理由 | 新版位置 |
|---|---|---|---|
| 1. Supply and Demand | 正式 | 合併生產與需求，修正披薩例子及無彈性定義。 | [供需、邊際產出、規模與彈性](economics.md#card-1) |
| 5. Diminishing Returns | 正式 | 合併生產與需求，修正披薩例子及無彈性定義。 | [供需、邊際產出、規模與彈性](economics.md#card-1) |
| 6. Economies of Scale | 正式 | 合併生產與需求，修正披薩例子及無彈性定義。 | [供需、邊際產出、規模與彈性](economics.md#card-1) |
| 11. Price Elasticity | 正式 | 合併生產與需求，修正披薩例子及無彈性定義。 | [供需、邊際產出、規模與彈性](economics.md#card-1) |
| 2. Opportunity Cost | 正式 | 合併資源配置，刪任意薪資及教育必四年所得。 | [機會成本、邊際判斷與比較優勢](economics.md#card-2) |
| 3. Marginal Thinking | 正式 | 合併資源配置，刪任意薪資及教育必四年所得。 | [機會成本、邊際判斷與比較優勢](economics.md#card-2) |
| 4. Comparative Advantage (Ricardo) | 正式 | 合併資源配置，刪任意薪資及教育必四年所得。 | [機會成本、邊際判斷與比較優勢](economics.md#card-2) |
| 7. Invisible Hand (Smith) | 啟發法 | 合併歷史性解釋，刪未核故事與引言。 | [Invisible Hand、Creative Destruction、Bubbles](economics.md#card-7) |
| 8. Creative Destruction (Schumpeter) | 啟發法 | 合併歷史性解釋，刪未核故事與引言。 | [Invisible Hand、Creative Destruction、Bubbles](economics.md#card-7) |
| 13. Bubbles and Crashes | 實證 | 合併歷史性解釋，刪未核故事與引言。 | [Invisible Hand、Creative Destruction、Bubbles](economics.md#card-7) |
| 9. Externalities | 正式 | 合併制度問題並加入共同治理反證。 | [外部性、市場失靈、公地與搭便車](economics.md#card-9) |
| 10. Market Failure | 正式 | 合併制度問題並加入共同治理反證。 | [外部性、市場失靈、公地與搭便車](economics.md#card-9) |
| 18. Tragedy of the Commons | 正式 | 合併制度問題並加入共同治理反證。 | [外部性、市場失靈、公地與搭便車](economics.md#card-9) |
| 19. Free Rider Problem | 正式 | 合併制度問題並加入共同治理反證。 | [外部性、市場失靈、公地與搭便車](economics.md#card-9) |
| 12. Arbitrage | 正式 | 保留，補摩擦與不等價問題。 | [套利 Arbitrage](economics.md#card-12) |
| 14. Incentives | 啟發法 | 合併資訊與契約機制，移除誘因決定結果的引言。 | [誘因、委託代理、道德風險與逆選擇](economics.md#card-14) |
| 15. Principal-Agent Problem | 正式 | 合併資訊與契約機制，移除誘因決定結果的引言。 | [誘因、委託代理、道德風險與逆選擇](economics.md#card-14) |
| 16. Moral Hazard | 正式 | 合併資訊與契約機制，移除誘因決定結果的引言。 | [誘因、委託代理、道德風險與逆選擇](economics.md#card-14) |
| 17. Adverse Selection | 正式 | 合併資訊與契約機制，移除誘因決定結果的引言。 | [誘因、委託代理、道德風險與逆選擇](economics.md#card-14) |
| 20. Subjective Value | 正式 | 合併價值發現，補定價與拍賣條件。 | [主觀價值、差別訂價、組合銷售與拍賣](economics.md#card-20) |
| 21. Price Discrimination | 正式 | 合併價值發現，補定價與拍賣條件。 | [主觀價值、差別訂價、組合銷售與拍賣](economics.md#card-20) |
| 22. Bundling | 正式 | 合併價值發現，補定價與拍賣條件。 | [主觀價值、差別訂價、組合銷售與拍賣](economics.md#card-20) |
| 26. Auctions and Price Discovery | 正式 | 合併價值發現，補定價與拍賣條件。 | [主觀價值、差別訂價、組合銷售與拍賣](economics.md#card-20) |
| 23. Network Effects | 正式 | 合併至 networks.md 主條目。 | [Network Effects、Two-Sided Markets、Switching Costs](economics.md#card-23) |
| 24. Two-Sided Markets | 正式 | 合併至 networks.md 主條目。 | [Network Effects、Two-Sided Markets、Switching Costs](economics.md#card-23) |
| 25. Switching Costs | 正式 | 合併至 networks.md 主條目。 | [Network Effects、Two-Sided Markets、Switching Costs](economics.md#card-23) |
