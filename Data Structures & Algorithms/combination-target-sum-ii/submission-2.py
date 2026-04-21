class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []
        
        # Sort so duplicates are adjacent — this is what makes skip logic work
        candidates.sort()

        def backtrack(i, total):
            # Found a valid combination — add a snapshot (copy) to results
            # Checked before the bounds/overshoot guard because the last
            # element added might have hit the target exactly
            if total == target:
                res.append(cur.copy())
                return

            # Out of elements, or current sum already exceeds target — prune
            if i >= len(candidates) or total > target:
                return

            # ── Branch 1: PICK candidates[i] ──────────────────────────────
            cur.append(candidates[i])
            backtrack(i + 1, total + candidates[i])  # advance index (each number used once)
            cur.pop()                                 # undo the pick (backtrack)

            # ── Branch 2: SKIP candidates[i] ─────────────────────────────
            # Skip ALL consecutive duplicates of candidates[i] so we don't
            # explore the same "don't pick this value" branch more than once.
            # Example: [1,1,2] — after deciding not to pick the first 1,
            # we jump past the second 1 too, avoiding duplicate subsets.
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, total)  # recurse from the next distinct value

        backtrack(0, 0)
        return res