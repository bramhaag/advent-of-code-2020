defmodule Day5B do
    def solve() do
        seat_ids = File.read!("input.txt")
        |> String.split("\n" , trim: true)
        |> Enum.map(&(split(&1, Enum.to_list(0..127), Enum.to_list(0..7))))

        {min_id, max_id} = Enum.min_max(seat_ids)
        Enum.sum(min_id..max_id) - Enum.sum(seat_ids)
    end

    def split("F" <> x, rows, columns), do: with {first, _} <- split_list(rows), do: split(x, first, columns)
    def split("B" <> x, rows, columns), do: with {_, last}  <- split_list(rows), do: split(x, last, columns)
    def split("L" <> x, rows, columns), do: with {first, _} <- split_list(columns), do: split(x, rows, first)
    def split("R" <> x, rows, columns), do: with {_, last}  <- split_list(columns), do: split(x, rows, last)
    def split(_, [row], [column]), do: row * 8 + column

    def split_list(list), do: Enum.split(list, div(length(list), 2))
end

Day5B.solve() |> IO.puts