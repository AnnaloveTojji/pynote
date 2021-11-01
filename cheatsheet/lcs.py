cache = {}
def lcs(s1, s2):
  global cache
  if len(s1) == 0 or len(s2) == 0:
      return 0
  if (s1, s2) in cache:
      return cache[(s1, s2)]
  else:
      if s1[-1] == s2[-1]:
          cache[(s1, s2)] = 1 + lcs(s1[:-1], s2[:-1])
      else:
          cache[(s1, s2)] = max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))
  return cache[(s1, s2)]