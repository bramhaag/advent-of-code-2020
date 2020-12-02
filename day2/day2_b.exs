defmodule Day2B do
    @password_regex ~r/(\d+)-(\d+) (.+): (.+)/
    
    def solve do
        File.read!("input.txt")
        |> String.split("\n" , trim: true)
        |> Enum.reduce(0, &(&2 + if is_valid?(&1), do: 1, else: 0))
        |> IO.puts
    end

    def is_valid?(input) do
        [password | [char | idx]] = Regex.run(@password_regex, input, capture: :all_but_first) |> Enum.reverse
        matches = idx
        |> Enum.map(&String.to_integer/1)
        |> Enum.map(&(String.at(password, &1 - 1) == char))
        true in matches and false in matches
    end
end

Day2B.solve