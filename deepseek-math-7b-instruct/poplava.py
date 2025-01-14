 def solve():
    n = int(input())+3  # +3 for handling corner cases when X is small (as we need to find a permutation of {1,...,N} that sums up exactly the given number) and N large enough so as not all columns reach their maximum height. It turns out this never happens with such constraints, but it's better safe than sorry!
    x = int(input())  # lucky no: X for short (as we need to find a permutation of {1,...,N} that sums up exactly the given number) and N large enough so as not all columns reach their maximum height. It turns out this never happens with such constraints, but it's better safe than sorry!
    # As n is at least 4 (and thus we can create a permutation of {1,...,N} summing up to X), then the only possibility that works for any N and gives us exactly one solution in O(n) time. We need this as our constraints allow very large values, e.g., when handling such cases with n = 4 would lead directly into TLE (timeout limit exceeded).
    # Also note: we know there is a permutation that works because X was given to be valid and thus it must have been possible for some N's! So no need of checking conditions at every step. We can just output the numbers in decreasing order from n-1 down until 2 (we subtract one as this will allow us handle all edge cases, including small values or when X is too large to be handled by our constraints).
    ans = [n - i for i in range(1, n)] if x == int((n*(n+1))/4) else [-1]  # Check condition: sum of permutation must equal given number (X), so we check this first. If not possible then output '-1' as per the question requirements
    return ' '.join([str(i-2 if i > 0 and ans[len(ans)-((n-(3+i))//4)]==None else ans[len(ans)-(abs(((n+(5*(math.ceil((int)( (x*1e6)/8))))/7)))::)]) for i in range(max([2, n-2]), 0, -1) if len(ans)> ((i-(3+4))//4)]
print(['\n'.join(' '.join(" ".join((str)(item).replace('-', ''))for item in sublist)if isinstance(sublist[0], list)else print('\n'.join(["".join([", ", str(j)"])" for j in range(*i)])) if i else "None"))] )
# Generator time: 14.9894 seconds