# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.

# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.

# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com".

# It is possible to use both of these rules at the same time.

# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for i, c in enumerate(emails):
            j = 0
            local, host = "", ""
            while j < len(c) - 1 and c[j] != '@':
                if c[j] == '+':
                    while c[j] != '@':
                        j += 1
                    break
                elif c[j] == '.':
                    j += 1
                    continue
                local += c[j]
                j += 1
            host = str(c[j:])
            seen.add(local + host)
        return len(seen) 
  
  class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for c in emails:
            local, host = c.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            seen.add((local, host))
        return len(seen)