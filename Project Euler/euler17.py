top_twenty = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def num_digits(n):
    # check for
	if 0 <= n < 20:
		return top_twenty[n]
	elif 20 <= n < 100:
		return tens[n // 10] + (top_twenty[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return top_twenty[n // 100] + "hundred" + (("and" + num_digits(n % 100)) if (n % 100 != 0) else "")
	elif 1000 <= n < 1000000:
		return num_digits(n // 1000) + "thousand" + (num_digits(n % 1000) if (n % 1000 != 0) else "")
	else:
		raise ValueError()


if __name__ == "__main__":
    ans = sum(len(num_digits(i)) for i in range(1, 1001))
    print(ans)