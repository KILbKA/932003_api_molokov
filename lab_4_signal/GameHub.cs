using Microsoft.AspNetCore.SignalR;
using System;
using System.Threading.Tasks;

public class GameHub : Hub
{
    private static int _numberToGuess;

    public GameHub()
    {
        if (_numberToGuess == 0)
        {
            // Инициализация игры
            _numberToGuess = new Random().Next(1, 100);
        }
    }

    public async Task GuessNumber(int userGuess)
    {
        if (userGuess == _numberToGuess)
        {
            await Clients.Caller.SendAsync("ReceiveMessage", "Поздравляем! Вы угадали число!");
            await Clients.Others.SendAsync("ReceiveMessage", $"Игрок {Context.ConnectionId} угадал число!");
            _numberToGuess = new Random().Next(1, 100); // Начинаем новый раунд
        }
        else
        {
            await Clients.Caller.SendAsync("ReceiveMessage", userGuess < _numberToGuess ? "Больше!" : "Меньше!");
        }
    }
}