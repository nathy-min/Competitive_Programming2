import string

class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        lower = set(string.ascii_lowercase)
        upper = set(string.ascii_uppercase)
        digits = set(string.digits)
        
        chars = set(s)
        
        missing_chars = 3 - (bool(chars & lower) + bool(chars & upper) + bool(chars & digits))
        required_type_replaces = int(missing_chars)
        
        required_inserts = max(0, 6 - len(s))
        required_deletes = max(0, len(s) - 20)
        
        groups = [len(list(grp)) for _, grp in itertools.groupby(s)]
        
        def apply_best_delete():
            argmin, _ = min(
                enumerate(groups),
                key=lambda it: it[1] % 3 if it[1] >= 3 else 10 - it[1],
            )
            groups[argmin] -= 1
        
        for _ in range(required_deletes):
            apply_best_delete()
        
        required_group_replaces = sum(group // 3 for group in groups)
        
        return (
            required_deletes +
            max(required_type_replaces, required_group_replaces, required_inserts)
        )
