# まずはwebスクレイピングを行う
# 必要なライブラリのインポート
from bs4 import BeautifulSoup
import requests
# タイムスリーパーをインストールする
import time



# アクセスしたいサイトのURLを変数に格納
url_a = 'https://tenki.jp/past/2023/12/19/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
a = requests.get (url_a)
a.encording = a.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
a_bs = BeautifulSoup(a.content, 'html.parser') 
# オブジェクトの表示
print(type(a_bs))

# 内容表示
a_bs

#sectionタグの'section-wrap'クラスの内容を探し出す
aa_bs = a_bs.find_all('section', class_='section-wrap')
# 内容表示
aa_bs

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
aaa_bs = a_bs.find_all('table', class_='amedas-point-detail-entries-table')
#内容表示
aaa_bs

# リストを作成
wet_td = []
# さらにtdタグを取り出す
for a_td in aaa_bs[0].select('td'):
    # テキストデータのみ抽出
    aa_td = a_td.text.strip()
    # リストに格納
    wet_td.append(aa_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[:4]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_b= 'https://tenki.jp/past/2023/12/20/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
b = requests.get (url_b)
b.encording = b.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
b_bs = BeautifulSoup(b.content, 'html.parser') 
# オブジェクトの表示
print(type(b_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
bbb_bs = b_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
bbb_bs

# tdタグを取り出す
for b_td in bbb_bs[0].select('td'):
    # テキストデータのみ抽出
    bb_td = b_td.text.strip()    
    # リストに格納
    wet_td.append(bb_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[1]
del wet_td[2:5]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_c= 'https://tenki.jp/past/2023/12/21/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
c = requests.get (url_c)
c.encording = c.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
c_bs = BeautifulSoup(c.content, 'html.parser') 
# オブジェクトの表示
print(type(c_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
ccc_bs = c_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
ccc_bs

# tdタグを取り出す
for c_td in ccc_bs[0].select('td'):
    # テキストデータのみ抽出
    cc_td = c_td.text.strip()   
    # リストに格納
    wet_td.append(cc_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[2]
del wet_td[3:6]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_d= 'https://tenki.jp/past/2023/12/22/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
d = requests.get (url_d)
d.encording = d.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
d_bs = BeautifulSoup(d.content, 'html.parser') 
# オブジェクトの表示
print(type(d_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
ddd_bs = d_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
ddd_bs

# tdタグを取り出す
for d_td in ddd_bs[0].select('td'):
    # テキストデータのみ抽出
    dd_td = d_td.text.strip()   
    # リストに格納
    wet_td.append(dd_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[3]
del wet_td[4:7]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_e = 'https://tenki.jp/past/2023/12/23/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
e = requests.get (url_e)
e.encording = e.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
e_bs = BeautifulSoup(e.content, 'html.parser') 
# オブジェクトの表示
print(type(d_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
eee_bs = e_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
eee_bs

# tdタグを取り出す
for e_td in eee_bs[0].select('td'):
    # テキストデータのみ抽出
    ee_td = e_td.text.strip()    
    # リストに格納
    wet_td.append(ee_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[4]
del wet_td[5:8]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_f = 'https://tenki.jp/past/2023/12/24/amedas/3/17/46091.html'

# HTMLを取得し表示
time.sleep(1)
f = requests.get (url_f)
f.encording = f.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
f_bs = BeautifulSoup(f.content, 'html.parser') 
# オブジェクトの表示
print(type(f_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
fff_bs = f_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
fff_bs

# tdタグを取り出す
for f_td in fff_bs[0].select('td'):
    # テキストデータのみ抽出
    ff_td = f_td.text.strip()  
    # リストに格納
    wet_td.append(ff_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[5]
del wet_td[6:9]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_g = 'https://tenki.jp/past/2023/12/25/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
g = requests.get (url_g)
g.encording = g.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
g_bs = BeautifulSoup(g.content, 'html.parser') 
# オブジェクトの表示
print(type(g_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
ggg_bs = g_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
ggg_bs

# tdタグを取り出す
for g_td in ggg_bs[0].select('td'):
    # テキストデータのみ抽出
    gg_td = g_td.text.strip()    
    # リストに格納
    wet_td.append(gg_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[6]
del wet_td[7:10]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_h = 'https://tenki.jp/past/2023/12/26/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
h = requests.get (url_h)
h.encording = h.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
h_bs = BeautifulSoup(h.content, 'html.parser') 
# オブジェクトの表示
print(type(h_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
hhh_bs = h_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
hhh_bs

# tdタグを取り出す
for h_td in hhh_bs[0].select('td'):
    # テキストデータのみ抽出
    hh_td = h_td.text.strip()   
    # リストに格納
    wet_td.append(hh_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[7]
del wet_td[8:11]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_i = 'https://tenki.jp/past/2023/12/27/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
i = requests.get (url_i)
i.encording = i.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
i_bs = BeautifulSoup(i.content, 'html.parser') 
# オブジェクトの表示
print(type(i_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
iii_bs = i_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
iii_bs

# tdタグを取り出す
for i_td in iii_bs[0].select('td'):
    # テキストデータのみ抽出
    ii_td = i_td.text.strip()   
    # リストに格納
    wet_td.append(ii_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[8]
del wet_td[9:12]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_j = 'https://tenki.jp/past/2023/12/28/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
j = requests.get (url_j)
j.encording = j.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
j_bs = BeautifulSoup(j.content, 'html.parser') 
# オブジェクトの表示
print(type(j_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
jjj_bs = j_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
jjj_bs

# tdタグを取り出す
for j_td in jjj_bs[0].select('td'):
    # テキストデータのみ抽出
    jj_td = j_td.text.strip()   
    # リストに格納
    wet_td.append(jj_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[9]
del wet_td[10:13]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_k = 'https://tenki.jp/past/2023/12/29/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
k = requests.get (url_k)
k.encording = k.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
k_bs = BeautifulSoup(k.content, 'html.parser') 
# オブジェクトの表示
print(type(k_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
kkk_bs = k_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
kkk_bs

# tdタグを取り出す
for k_td in kkk_bs[0].select('td'):
    # テキストデータのみ抽出
    kk_td = k_td.text.strip()   
    # リストに格納
    wet_td.append(kk_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[10]
del wet_td[11:14]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_l = 'https://tenki.jp/past/2023/12/30/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
l = requests.get (url_l)
l.encording = l.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
l_bs = BeautifulSoup(l.content, 'html.parser') 
# オブジェクトの表示
print(type(l_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
lll_bs = l_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
lll_bs

# tdタグを取り出す
for l_td in lll_bs[0].select('td'):
    # テキストデータのみ抽出
    ll_td = l_td.text.strip()   
    # リストに格納
    wet_td.append(ll_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[11]
del wet_td[12:15]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_m = 'https://tenki.jp/past/2023/12/31/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
m = requests.get (url_m)
m.encording = m.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
m_bs = BeautifulSoup(m.content, 'html.parser') 
# オブジェクトの表示
print(type(m_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
mmm_bs = m_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
mmm_bs

# tdタグを取り出す
for m_td in mmm_bs[0].select('td'):
    # テキストデータのみ抽出
    mm_td = m_td.text.strip()   
    # リストに格納
    wet_td.append(mm_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[12]
del wet_td[13:16]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_n = 'https://tenki.jp/past/2024/01/01/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
n = requests.get (url_n)
n.encording = n.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
n_bs = BeautifulSoup(n.content, 'html.parser') 
# オブジェクトの表示
print(type(n_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
nnn_bs = n_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
nnn_bs

# tdタグを取り出す
for n_td in nnn_bs[0].select('td'):
    # テキストデータのみ抽出
    nn_td = n_td.text.strip()    
    # リストに格納
    wet_td.append(nn_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[13]
del wet_td[14:17]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_o = 'https://tenki.jp/past/2024/01/02/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
o = requests.get (url_o)
o.encording = o.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
o_bs = BeautifulSoup(o.content, 'html.parser') 
# オブジェクトの表示
print(type(o_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
ooo_bs = o_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
ooo_bs

# tdタグを取り出す
for o_td in ooo_bs[0].select('td'):
    # テキストデータのみ抽出
    oo_td = o_td.text.strip()    
    # リストに格納
    wet_td.append(oo_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[14]
del wet_td[15:18]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_p = 'https://tenki.jp/past/2024/01/03/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
p = requests.get (url_p)
p.encording = p.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
p_bs = BeautifulSoup(p.content, 'html.parser') 
# オブジェクトの表示
print(type(p_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
ppp_bs = p_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
ppp_bs

# tdタグを取り出す
for p_td in ppp_bs[0].select('td'):
    # テキストデータのみ抽出
    pp_td = p_td.text.strip()   
    # リストに格納
    wet_td.append(pp_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[15]
del wet_td[16:19]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_q = 'https://tenki.jp/past/2024/01/04/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
q = requests.get (url_q)
q.encording = q.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
q_bs = BeautifulSoup(q.content, 'html.parser') 
# オブジェクトの表示
print(type(q_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
qqq_bs = q_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
qqq_bs

# tdタグを取り出す
for q_td in qqq_bs[0].select('td'):
    # テキストデータのみ抽出
    qq_td = q_td.text.strip()   
    # リストに格納
    wet_td.append(qq_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[16]
del wet_td[17:20]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_r = 'https://tenki.jp/past/2024/01/05/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
r = requests.get (url_r)
r.encording = r.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
r_bs = BeautifulSoup(r.content, 'html.parser') 
# オブジェクトの表示
print(type(r_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
rrr_bs = r_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
rrr_bs

# tdタグを取り出す
for r_td in rrr_bs[0].select('td'):
    # テキストデータのみ抽出
    rr_td = r_td.text.strip()   
    # リストに格納
    wet_td.append(rr_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[17]
del wet_td[18:21]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_s = 'https://tenki.jp/past/2024/01/06/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
s = requests.get (url_s)
s.encording = s.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
s_bs = BeautifulSoup(s.content, 'html.parser') 
# オブジェクトの表示
print(type(s_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
sss_bs = s_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
sss_bs

# tdタグを取り出す
for s_td in sss_bs[0].select('td'):
    # テキストデータのみ抽出
    ss_td = s_td.text.strip()    
    # リストに格納
    wet_td.append(ss_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[18]
del wet_td[19:22]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_t = 'https://tenki.jp/past/2024/01/07/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
t = requests.get (url_t)
t.encording = t.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
t_bs = BeautifulSoup(t.content, 'html.parser') 
# オブジェクトの表示
print(type(t_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
ttt_bs = t_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
ttt_bs

# tdタグを取り出す
for t_td in ttt_bs[0].select('td'):
    # テキストデータのみ抽出
    tt_td = t_td.text.strip()   
    # リストに格納
    wet_td.append(tt_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[19]
del wet_td[20:23]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_u = 'https://tenki.jp/past/2024/01/08/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
u = requests.get (url_u)
u.encording = u.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
u_bs = BeautifulSoup(u.content, 'html.parser') 
# オブジェクトの表示
print(type(u_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
uuu_bs = u_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
uuu_bs

# tdタグを取り出す
for u_td in uuu_bs[0].select('td'):
    # テキストデータのみ抽出
    uu_td = u_td.text.strip()    
    # リストに格納
    wet_td.append(uu_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[20]
del wet_td[21:24]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_v = 'https://tenki.jp/past/2024/01/09/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
v = requests.get (url_v)
v.encording = v.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
v_bs = BeautifulSoup(v.content, 'html.parser') 
# オブジェクトの表示
print(type(v_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
vvv_bs = v_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
vvv_bs

# tdタグを取り出す
for v_td in vvv_bs[0].select('td'):
    # テキストデータのみ抽出
    vv_td = v_td.text.strip()    
    # リストに格納
    wet_td.append(vv_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[21]
del wet_td[22:25]
# 内容表示
wet_td



# アクセスしたいサイトのURLを変数に格納
url_w = 'https://tenki.jp/past/2024/01/10/amedas/3/17/46091.html'
# HTMLを取得し表示
time.sleep(1)
w = requests.get (url_w)
w.encording = w.apparent_encoding

# HTMLソースをBeautifulSoupオブジェクトに変換する
w_bs = BeautifulSoup(w.content, 'html.parser') 
# オブジェクトの表示
print(type(w_bs))

# tableタグの'amedas-point-detail-entries-table'クラスの内容を探し出す
www_bs = w_bs.find_all('table', class_='amedas-point-detail-entries-table')
# 内容表示
www_bs

# tdタグを取り出す
for w_td in www_bs[0].select('td'):
    # テキストデータのみ抽出
    ww_td = w_td.text.strip()    
    # リストに格納
    wet_td.append(ww_td)
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[22]
del wet_td[23:26]
# 内容表示
wet_td

# 不要なデータを削除
del wet_td[0]
del wet_td[22]
# 内容表示
wet_td

