namespace myapp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var Products = new List<int> { 5, 6, 7, 10 };
            var q = from p in Products where p > 6 select p;
            foreach (var item in q)
            {
                Console.WriteLine(item); 
            }

        }
    }
}
