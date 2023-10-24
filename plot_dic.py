from syncmer_count_noverlap import return_syncmer_results
import matplotlib.pyplot as plt

df = return_syncmer_results()
x = df.iloc[:,0]

line1 = df["mash_containment_human"]
line2 = df["mash_containment_none_human"]
line3 = df["blast"]

plt.plot(x, line1, marker='o', label='containment_human')
plt.plot(x, line2, marker='s', label='containment_none_human')
plt.plot(x, line3, marker='^', label='blast')

plt.title('Syncmer VS Blast')
plt.xlabel('Species')
plt.ylabel('ANI')

plt.legend()
plt.savefig('./1.jpg')
plt.show()
