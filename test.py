import sqlite3

def connect():
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        print("DataBase Connected")
    except:
        print("Database Error")
        return None,None
    return cursor, con


cursor,con = connect()
query = """insert into contest values('reposts','<dd><p>One day Polycarp published a funny picture in a social network making a poll about the color of his handle. Many of his friends started reposting Polycarps joke to their news feed. Some of them reposted the reposts and so on.</p>
<p>These events are given as a sequence of strings "<span class="tex-font-style-it">name1</span> <span class="tex-font-style-tt">reposted</span> <span class="tex-font-style-it">name2</span>", where <span class="tex-font-style-it">name1</span> is the name of the person who reposted the joke, and <span class="tex-font-style-it">name2</span> is the name of the person from whose news feed the joke was reposted. It is guaranteed that for each string "<span class="tex-font-style-it">name1</span> <span class="tex-font-style-tt">reposted</span> <span class="tex-font-style-it">name2</span>" user "<span class="tex-font-style-it">name1</span>" didnt have the joke in his feed yet, and "<span class="tex-font-style-it">name2</span>" already had it in his feed by the moment of repost. Polycarp was registered as "<span class="tex-font-style-tt">Polycarp</span>" and initially the joke was only in his feed.</p>
<p>Polycarp measures the popularity of the joke as the length of the largest repost chain. Print the popularity of Polycarps joke.</p></dd>','<dd><p>The first line of the input contains integer <span class="tex-span"><i>n</i></span> (<span class="tex-span">1 ≤ <i>n</i> ≤ 200</span>) — the number of reposts. Next follow the reposts in the order they were made. Each of them is written on a single line and looks as "<span class="tex-font-style-it">name1</span> <span class="tex-font-style-tt">reposted</span> <span class="tex-font-style-it">name2</span>". All the names in the input consist of lowercase or uppercase English letters and/or digits and have lengths from 2 to 24 characters, inclusive.</p>
<p>We know that the user names are case-insensitive, that is, two names that only differ in the letter case correspond to the same social network user.</p></dd>','<dd><p>Print a single integer — the maximum length of a repost chain.</p></dd>','<table class="vjudge_sample">
<thead>
  <tr>
    <th>Input<span class="copier">copy</span></th>
    <th>Output<span class="copier">copy</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><pre>5
tourist reposted Polycarp
Petr reposted Tourist
WJMZBMR reposted Petr
sdya reposted wjmzbmr
vepifanov reposted sdya
</pre></td>
    <td><pre>6
</pre></td>
  </tr>
</tbody>
</table>')"""
cursor.execute(query)