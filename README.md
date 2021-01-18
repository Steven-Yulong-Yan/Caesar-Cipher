# Caesar-Cipher

This is an implementation of Caesar Cipher. Text is encrypted with a simple cipher where each letter of the alphabet is replaced with another letter that occurs a fixed number of letters later.
This fixed number is known as the coding offset. The program accepts 0 as an input when a shift offset is requested.
If the user types this, encrypted/decrypted text will be shown for all offsets (1 to 25, inclusive).
The program accepts all characters (not just English letters and spaces). These characters will be ignored when encrypting or decrypting.
When automatically decrypting English text, the program will ignore contractions (words containing an apostrophe - i.e. we're, you've, goose's, etc) and
treat words joined together by a hyphen or dash as separate words (i.e. sea-song is treated as two words: sea & song).

## Example Output

```
Welcome to the simple encryption tool!

Please choose an option [e/d/a/q]:
  e) Encrypt some text
  d) Decrypt some text
  a) Automatically decrypt English text
  q) Quit
> e
Please enter some text to encrypt: you will always remember this as the day
Please enter a shift offset (1-25): 7
The encrypted text is: fvb dpss hsdhfz yltltily aopz hz aol khf

Please choose an option [e/d/a/q]:
  e) Encrypt some text
  d) Decrypt some text
  a) Automatically decrypt English text
  q) Quit
> d

Please enter some text to decrypt: asdf ghjkl qwerty uiop z xcvbnm
Please enter a shift offset (1-25): 17
The decrypted text is: jbmo pqstu zfnach drxy i glekwv

Please choose an option [e/d/a/q]:
  e) Encrypt some text
  d) Decrypt some text
  a) Automatically decrypt English text
  q) Quit
> d

Please enter some text to decrypt: a bmkl kso lzw sv sfv lzgmyzl al dggcwv xmf
Please enter a shift offset (1-25): 18
The decrypted text is: i just saw the ad and thought it looked fun

Please choose an option [e/d/a/q]:
  e) Encrypt some text
  d) Decrypt some text
  a) Automatically decrypt English text
  q) Quit
> ep zpv tff uiptf uxp xffwjmt epdups
Invalid command

Please choose an option [e/d/a/q]:
  e) Encrypt some text
  d) Decrypt some text
  a) Automatically decrypt English text
  q) Quit
> a
Please enter some encrypted text: ep zpv tff uiptf uxp xffwjmt epdups
Encryption offset: 1
Decrypted message: do you see those two weevils doctor

Please choose an option [e/d/a/q]:
  e) Encrypt some text
  d) Decrypt some text
  a) Automatically decrypt English text
  q) Quit
> a
Please enter some encrypted text: nmd
Multiple encryption offsets: 4, 12, 21, 25

Please choose an option [e/d/a/q]:
  e) Encrypt some text
  d) Decrypt some text
  a) Automatically decrypt English text
  q) Quit
> a
Please enter some encrypted text: asdf ghjkl qwerty uiop z xcvbnm
No valid encryption offset

Please choose an option [e/d/a/q]:
  e) Encrypt some text
  d) Decrypt some text
  a) Automatically decrypt English text
  q) Quit
> e
Please enter some text to encrypt: all we can do is smile back
Please enter a shift offset (1-25): 0
The encrypted text is:
  01: bmm xf dbo ep jt tnjmf cbdl
  02: cnn yg ecp fq ku uokng dcem
  03: doo zh fdq gr lv vploh edfn
  04: epp ai ger hs mw wqmpi fego
  05: fqq bj hfs it nx xrnqj gfhp
  06: grr ck igt ju oy ysork hgiq
  07: hss dl jhu kv pz ztpsl ihjr
  08: itt em kiv lw qa auqtm jiks
  09: juu fn ljw mx rb bvrun kjlt
  10: kvv go mkx ny sc cwsvo lkmu
  11: lww hp nly oz td dxtwp mlnv
  12: mxx iq omz pa ue eyuxq nmow
  13: nyy jr pna qb vf fzvyr onpx
  14: ozz ks qob rc wg gawzs poqy
  15: paa lt rpc sd xh hbxat qprz
  16: qbb mu sqd te yi icybu rqsa
  17: rcc nv tre uf zj jdzcv srtb
  18: sdd ow usf vg ak keadw tsuc
  19: tee px vtg wh bl lfbex utvd
  20: uff qy wuh xi cm mgcfy vuwe
  21: vgg rz xvi yj dn nhdgz wvxf
  22: whh sa ywj zk eo oieha xwyg
  23: xii tb zxk al fp pjfib yxzh
  24: yjj uc ayl bm gq qkgjc zyai
  25: zkk vd bzm cn hr rlhkd azbj
 
Please choose an option [e/d/a/q]:
  e) Encrypt some text
  d) Decrypt some text
  a) Automatically decrypt English text
  q) Quit
> a
Please enter some encrypted text: X gtbtbqtg wxb addzxcv gdjcs iwt rdktg pcs lwxhiaxcv id wxbhtau ph wt sxs hd, pcs iwtc qgtpzxcv dji xc iwpi das htp-hdcv iwpi wt hpcv hd duitc puitglpgsh: "Uxuittc btc dc iwt stps bpc'h rwthi; Nd- wd-wd, pcs p qdiiat du gjb!"
Encryption offset: 15
Decrypted message: I remember him looking round the cover and whistling to himself as he did so, and then breaking out in that old sea-song that he sang so often afterwards: "Fifteen men on the dead man's chest; Yo-ho-ho, and a bottle of rum!"

Please choose an option [e/d/a/q]:
  e) Encrypt some text
  d) Decrypt some text
  a) Automatically decrypt English text
  q) Quit
> q
Bye!
```
