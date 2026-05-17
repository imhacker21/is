<!DOCTYPE html>
<html>

<body>

    <input type="number" id="p" placeholder="Prime number">

    <input type="number" id="g" placeholder="Base">

    <input type="number" id="a" placeholder="Alice private key">

    <button onclick="generateKey()">
        Generate Shared Key
    </button>

    <h3 id="result"></h3>

    <script>

        function power(b, e, m) {

            let r = 1;

            while (e > 0) {

                if (e % 2 == 1)
                    r = (r * b) % m;

                b = (b * b) % m;

                e = Math.floor(e / 2);
            }

            return r;
        }

        function generateKey() {

            let p = +document.getElementById("p").value;

            let g = +document.getElementById("g").value;

            let a = +document.getElementById("a").value;

            let b = Math.floor(Math.random() * 10) + 1;

            let A = power(g, a, p);

            let B = power(g, b, p);

            let key1 = power(B, a, p);

            let key2 = power(A, b, p);

            document.getElementById("result").innerHTML =
                "Bob Key: " + b + "<br>" +
                "Alice Public: " + A + "<br>" +
                "Bob Public: " + B + "<br><br>" +
                "Alice Shared Key: " + key1 + "<br>" +
                "Bob Shared Key: " + key2;
        }

    </script>

</body>

</html>