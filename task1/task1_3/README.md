# awesome_cat_cat writeup

::: 

Challenge link: https://ctf.viblo.asia/puzzles/awesome-cat-cat-vsh4lnibh4i

Challenge name: awesome_cat_cat

Challenge desc: Looking in cat's eyes, it not just cat but also stores something strange. Can you find it ?

ISO/IEC 10918-1File provided: awesome_cat_cat.zip

:::

* unzip **awesome_cat_cat.zip**
* After unzipping I obtained **It_just_a_little_cat.jpeg**, I confirmed its format using
`file It_just_a_little_cat.jpeg`
* At first I tried some basic tools such as
    * binwalk
    * zsteg
    * steghide
    * stegsolve 
* Apparently they revealed nothing
* I also tried messing around with GIMP, using gimp to extract it as .png and compare it to the original .jpeg

`compare It_just_a_little_cat.jpeg It_just_a_little_cat.png diff.png`

<img src="https://hackmd.io/_uploads/B120X_0VZx.png" width="400" />

* I attempted to extract LSB, after a while I decided to move on from this approach because it is a jpeg after all, you can't do LSB on non-lossless image. The pattern was just coincidental
* Returning to binwalk, I noticed there was an option to analyze the entropy of the image
`binwalk -E It_just_a_little_cat.jpeg`

<img src="https://hackmd.io/_uploads/Byv6Su04Ze.png" width="400" />

* At the end the entropy value plummeted, which is suspicious
* Back to when I attempted to open the .jpeg with GIMP, there was a warning
> Corrupt JPEG data: 20273 extraneous bytes before marker 0xd9
* The file has in total 210049 bytes so I tried to use dd with the offset: 210049-(20273+2) 
`dd if=It_just_a_little_cat.jpeg of=cat.bin bs=1 skip=189774`
* However, after experimenting around with the data for a while I yielded no results
> Only until I got the hint to expand the image did I got an idea
* .jpeg files are made of markers, starting with FF and followed by with a byte that indicate the marker type
![image](https://hackmd.io/_uploads/SyEz9uR4Zg.png)
* I know this is baseline through the use of the "file" command

![image](https://hackmd.io/_uploads/rkIthORNbe.png)
* I used hexeditor and searched for **FF C0**, modified the 4th byte after FF C0 to a larger value. Opening the modified .jpeg reveals the flag

![image](https://hackmd.io/_uploads/HJnxauCNWl.png)

**Flag{c4t_c4t_1s_ju5t_f1nger_pr1nt}**

---
