n=int(input('masukkan banyaknya bilangan:'))
sigma_x=0
for i in range (1,n+1):
    x=float(input('masukkan bilangan ke-%d:'%i))
    sigma_x = sigma_x+ x
print ('rata-rata = %d'%(sigma_x/n))