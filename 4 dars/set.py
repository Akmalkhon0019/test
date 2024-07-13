'''1. Set e'lon qilish uchun set sinfidan foydalaniladi. Ya`ni set 
sinfidan object olamiz!

Set bu unikal kalit qiymatga ega bo'lgan to'plam.

2. add() - setga element qo'shish uchun ishlatiladi.
M: st = {1,2,3,4} st.add(5) st = {1,2,3,4,5}

3. update() - Ikkala to'plamdagi elementlarni birlashtirish uchun
ishlatiladi, bunda takrorlangan elementlar faqat bittasini qoldiradi.
(setga element (qo'shish) uchun ishlatiladi.)
 M: st = {1,2,3,4} st.update([5,6,7,8]) st = {1,2,3,4,5,6,7,8}

 4. union() - Ikkala to'plam elementlarini birlashganini qaytaradi,
 bunda takrorlangan elementlar faqat bittasi qoldiriladi.

 5. remove(x) - Setdan x elementni agar bor bo'lsa o'chiradi, aks holatda
 aks holatda xatolik qaytaradi.
 M: st = {1,2,3,4} st.remove(3) st = {1,2,4}

 6. pop() - setdan elementni o'chirish uchun ishlatiladi.
 M: st = {1,2,3,4} st.pop() st = {2,3,4}

 7. s1.intersection(s2) - s1 va s2 to'plamning o'zaro
 elementlarini qaytaradi.
 M: s1 = {1,2,3,4} s2 = {3,4,5,6} s1.intersection(s2) = {3,4}

 8. st.discard(x) - ko'rsatilgan to'plamdan x qiymatdagi elementni
 o'chirish uchun ishlatiladi. agar element mavjud bo'lmasa, xatolik
 bermaydi.
 M: st = {1,2,3,4} st.discard(3) st = {1,2,4}

 9. st.clear() - setni bo'sh qilish uchun ishlatiladi.

 10. st.count(x) - Setda x elementning uchrashlar sonini qaytaradi,
 bu maximum = 1 minimum = 0 bo'lishi mumkin.
 M: st = {1,2,3,4} st.count(3) = 1

11. s1.diffence(s2) - s1 va s2 to'plamning farqini s1 to'plamga nisbatan
 qaytaradi.
 M: s1 = {1,2,3,4} s2 = {3,4,5,6} s1.diffence(s2) = {1,2}

12.
13.
14.
15. s1.issubset(s2) - s1 to'plam elementlarini s2 to'plamning 
 o'zaro elementlariga ega bo'lganligini tekshiradi.
 M: s1 = {1,2,3,4} s2 = {3,4,5,6} s1.issubset(s2) = True
 M: s1 = {1,2,3,4} s2 = {3,4,5,6,7} s1.issubset(s2) = False
 M: s1 = {1,2,3,4} s2 = {3,4,5,6} s1.issuperset(s2) = False

 16. s1.isdisjoint(s2) - ushbu funksiya s1 va s2 to'plamlarning
 o'zaro kesishgan elementi mavjud bo'lsa false, aks holatda true qiymat qaytaradi
 M: s1 = {1,2,3,4} s2 = {3,4,5,6} s1.isdisjoint(s2) = False
 M: s1 = {1,2,3,4} s2 = {3,4,5,6,7} s1.isdisjoint(s2) = True
 M: s1 = {1,2,3,4} s2 = {3,4,5,6} s1.issuperset(s2) = False
 M: s1 = {1,2,3,4} s2 = {3,4,5,6,7} s1.issuperset(s2) = False 
