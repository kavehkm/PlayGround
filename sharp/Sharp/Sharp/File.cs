using System;
using System.IO;


namespace Sharp
{
    class Files
    {
        private string path;

        public Files(string path)
        {
            this.path = path;
        }

        public void Write(string text)
        {
            File.WriteAllText(path, text);
        }

        public string Read()
        {
            return File.ReadAllText(path);
        }
    }
}
