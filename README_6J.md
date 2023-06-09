# 精銳矩陣計算求解器(Sharp Matrix Solver, SMS)驗證  

## 測試實例採用 : Jagmohan L. Humar, "Dynamics of Structures Third Editon"  

### Example 10.3 第502頁 至 504頁，作爲SMS實作驗證  

M * y$_h$''(t) + C * y$_h$'(t) + K * y$_h$(t) = 0  . . . . . (A)  

已知數據如右: M = [2 0] | [0 1],  C = [3 -1] | [-1 1], K = [0.4 -0.5] | [0.5 0.2]  

即 :  

$M=\left(\begin{array}{lr}2 & 0 \\ 0 & 1 \end{array}\right)$  

$C=\left(\begin{array}{lr}3 & -1 \\ -1 & 1 \end{array}\right)$  

$K=\left(\begin{array}{lr}0.4 & -0.5 \\ 0.5 & 0.2 \end{array}\right)$  

SMS的陣列(Array)運算子(Operator) 共有十二個，即  

+, -, *, /, ==, !=, &, |, ^, !, ~, +(unit operator)等計有十二個。  

> "+"，"-"，"*"，"/"表示陣列的加、減、乘和除的運算子，
> "=="和"!="表示陣列相等否？，傳回bool值，
> "&"表示陣列的水平合併，"|"表示陣列的垂直合併，"^"向量内積，
> "!"陣列轉置，"~"方陣求逆，"+"單位向量等等的運算子。
> 上述的陣列運算子，適用於複數和實數陣列運算。複數與實數的轉換稱作Implicit and Explicit Converter。

方程式(A)式中，(y$_h$，Subscript h代表Homogeneous Solution)其變位與速度的響應值為(但本書缺少加速度響應值) :  

y$_h$0(t) = Exp(-0.08334t)*[1.00028*Cos(0.70221t) + 0.11076*Sin(0.70221t)] +
           Exp(-0.11667t)*[-0.00028*Cos(1.40933t) + 0.00395*Sin(1.40933t)] . . .(1)  

y$_h$1(t) = Exp(-0.08334t)*[1.99983*Cos(0.70221t) + 0.24528*Sin(0.70221t)] +
         Exp(-0.11667t)*[0.00019*Cos(1.40933t) - 0.00395*Sin(1.40933t)] . . .(2)  

y$_h$'0(t) = Exp(-0.08334t)*[-0.00558*Cos(0.70221t) - 0.71164*Sin(0.70221t)] +
         Exp(-0.11667t)*[0.00559*Cos(1.40933t) - 0.000066*Sin(1.40933t)] . . .(3)  

y$_h$'1(t) = Exp(-0.08334t)*[-0.00558*Cos(0.70221t) - 1.42474*Sin(0.70221t)] +
         Exp(-0.11667t)*[0.00559*Cos(1.40933t) + 0.000193*Sin(1.40933t)] . . .(4)  

### 公式(A)與SMS測試的結果完全相同  
