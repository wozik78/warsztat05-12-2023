try:
    print("12"+34)
except TypeError:
    print("blad typu")
except ZeroDivisionError:
    print("nie dziel przez zero!!!")
except Exception as e:
    print("blad",e)
else:
    print("wykona sie gdy nie ma błędu")
finally:
    print("Wykona sie zawsze")

print("dalsza częścć programu")

