defmodule Day2A do
    @password_regex ~r/(\d+)-(\d+) (.+): (.+)/

    def solve do
        File.read!("input.txt")
        |> String.split("\n" , trim: true)
        |> Enum.reduce(0, &(&2 + if is_valid?(&1), do: 1, else: 0))
        |> IO.puts
    end

    def is_valid?(input) do
        [min, max, char, password] = Regex.run(@password_regex, input, capture: :all_but_first)
        {min, _} = min |> Integer.parse
        {max, _} = max |> Integer.parse
        char_count = (password |> String.split(char) |> length()) - 1
        char_count in min..max
    end
end

Day2A.solve