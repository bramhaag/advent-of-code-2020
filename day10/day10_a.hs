import Data.List

main = do
    content <- readFile "input.txt"
    let adapters = sort $ map (read::String->Int) $ lines content
    let differences = zipWith (-) adapters (0 : adapters) ++ [3]
    print $ count 3 differences * count 1 differences

count :: Int -> [Int] -> Int
count x = length . filter(==x)