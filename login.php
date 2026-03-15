<?php
// Carrega o arquivo XML
$xml = simplexml_load_file("usuarios.xml");

if (isset($_POST['login'])) {
    $user = $_POST['user'];
    $pass = $_POST['pass'];

    // CONSULTA VULNERÁVEL: Os dados são inseridos diretamente na query
    $query = "//usuario[nome/text()='$user' and senha/text()='$pass']";
    
    $resultado = $xml->xpath($query);

    if ($resultado) {
        echo "<h1>Bem-vindo, " . $resultado[0]->nome . "!</h1>";
        echo "<p>Tipo de conta: " . $resultado[0]->tipo . "</p>";
    } else {
        echo "<p style='color:red;'>Login ou senha incorretos.</p>";
    }
}
?>

<form method="POST">
    Login: <input type="text" name="user"><br>
    Senha: <input type="password" name="pass"><br>
    <input type="submit" name="login" value="Entrar">
</form>
