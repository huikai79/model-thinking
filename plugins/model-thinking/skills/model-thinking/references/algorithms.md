# 演算法參考

只讀與問題相關的卡片。正式、實證、啟發法的分類與查核狀態見 [來源紀錄](sources.md)。合併卡片保留不同動作，不代表各概念互為證據。

<a id="card-1"></a>
## 最佳停止 Optimal Stopping／Secretary Problem

**性質：正式。** 經典秘書問題：已知總數 n、隨機順序、只能看相對排名、拒絕不可回頭，目標是最大化選到唯一最佳者的機率。大 n 時先略過約 n/e，再選首個超過此前最佳者；有限 n 門檻需另算。

**適用限制：** 37% 不是適用招聘、伴侶、租屋的普遍最佳比例；可回頭、未知總數、不同效用或搜尋成本會改變解。Look-Then-Leap 僅是相關啟發。

來源／查核狀態：[FERGUSON](sources.md#ferguson)。

<a id="card-4"></a>
## Bandit、Explore／Exploit、Gittins Index

**性質：正式。** 反覆選擇會同時產生收益與資訊；比較試新選項的資訊價值與既有收益。Gittins 定理適用特定獨立、折現且未選取臂狀態不變的 bandit 設定。

**適用限制：** 不能把任意新人加分當 Gittins 最優解；非平穩、互相影響、有限期限等需另分析。年齡不決定探索比例。

來源／查核狀態：[FERGUSON](sources.md#ferguson)。

<a id="card-7"></a>
## Comparison Sorts、Bucket Sort

**性質：正式。** 有一致的比較規則時可用 merge sort 等排序；bucket sort 先依鍵值區間分桶，再於桶內排序。

**適用限制：** 主觀偏好可能不傳遞；任意分成喜歡／不喜歡只屬分類類比，不自動繼承 bucket sort 的效率。

來源／查核狀態：[FOUNDATION](sources.md#foundation)。

<a id="card-9"></a>
## Search Costs、LRU、Noguchi Filing

**性質：啟發法。** 比較整理與找回成本；若近期使用可預測下次需求，可把近期資料放前面。LRU 快取淘汰最久未使用者。

**適用限制：** LRU 的效果依存取模式，循環掃描可能使它失效；紙本移到最前不等於最佳分類。本次未核實 Noguchi 原書。

來源／查核狀態：[EDITORIAL](sources.md#editorial)。

<a id="card-12"></a>
## 排程 EDD、SJF、Weighted SJF

**性質：正式。** 單機、全部工作已可開始、無前置相依、處理時間已知時：EDD 按到期日減少最大 lateness；SJF 按工時減少總完成時間；Smith’s rule 按 pᵢ/wᵢ 排序減少加權總完成時間。

**適用限制：** EDD 不要求等長。工作釋出時間、可搶占、相依、多資源、權重非固定時，這些保證可能不成立；產品 WSJF 的延遲成本估計另需檢驗。

來源／查核狀態：[SCHEDULING](sources.md#scheduling)。

<a id="card-15"></a>
## 阻塞、批次與切換 Priority Inversion、Coalescing、Thrashing

**性質：啟發法。** 先畫資源等待鏈；低優先工作持有高優先工作所需資源時可能發生 priority inversion。可批次處理低急迫中斷，限制同時工作量。

**適用限制：** 不是每個拖延都算優先反轉；批次增加等待，減少並行也可能降低吞吐。人的注意力類比不直接繼承作業系統定理。

來源／查核狀態：[EDITORIAL](sources.md#editorial)。

<a id="card-19"></a>
## Gradient Descent、Hill Climbing、Simulated Annealing、Random Restarts

**性質：正式。** 有目標函式時，gradient descent 沿負梯度更新；hill climbing 比較鄰近解；annealing 以溫度控制接受較差解的機率；重啟可探索其他起點。

**適用限制：** 步長、光滑性、凸性、鄰域及退火排程影響保證；隨機不是必較佳，產品改進沒有可量測目標時只可當類比。

來源／查核狀態：[BOYD](sources.md#boyd)。

<a id="card-23"></a>
## 約束與鬆弛 Constraint Satisfaction、Relaxation、Lagrangian Relaxation

**性質：正式。** 先找滿足硬限制的可行解；鬆弛較難限制取得界限或候選解。Lagrangian 將限制乘以乘子加入目標並形成對偶問題，用於界限或求解。

**適用限制：** 鬆弛解可能不可行，最後仍須檢查原限制；Lagrangian 不等於允許任意花錢違反硬限制，強對偶也需條件。

來源／查核狀態：[BOYD](sources.md#boyd)。
