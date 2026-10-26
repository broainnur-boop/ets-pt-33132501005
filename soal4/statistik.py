def rentang(data):
    return (min(data), max(data))


def ringkasan(data):
    return {
        "jumlah": len(data),
        "min": min(data),
        "maks": max(data),
        "rata": sum(data) / len(data)
    }


data = [12.0, 15.0, 15.0]

hasil_rentang = rentang(data)
r = ringkasan(data)

print(hasil_rentang)
print(r)
print(r["rata"])