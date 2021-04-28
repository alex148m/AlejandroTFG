for i = 2, . . . , m do
  Find Tr(H_i−1)
  Compute Tr(H_i) = Min(Tr(H_i−1)
  union {{v}, v ∈ E_i })
end for
Return Tr(Hm)
