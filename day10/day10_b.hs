import Data.List

main = do
    content <- readFile "input.txt"
    let adapters = sort $ map (read::String->Int) $ lines content
    let differences = zipWith (-) adapters (0 : adapters) ++ [3]
    let trib_n = idx 3 $ zip [1..] differences
    print $ product $ map trib $ map (subtract 1) $ zipWith (-) trib_n (0 : trib_n)

idx :: Int -> [(Int, Int)] -> [Int]
idx x ((i, d):xs) 
    | x == d    = i : xs'
    | otherwise = xs'
    where xs' = idx x xs
idx _ _ = []

trib :: Int -> Int
trib 0 = 1
trib 1 = 1
trib 2 = 2
trib n = trib(n - 1) + trib(n - 2) + trib(n - 3)
