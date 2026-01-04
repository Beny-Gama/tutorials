# Como fazer um Pull Request?

### 1️⃣ Você cria uma branch

```bash
git checkout -b minha-feature
```

### 2️⃣ Você escreve código e faz commit

```bash
git add .
git commit -m "Minha nova funcionalidade"
```

### 3️⃣ Você envia a branch para o repositório remoto

```bash
git push origin minha-feature
```

### 4️⃣ Você abre um Pull Request (GitHub / GitLab / Bitbucket)

- No site aparece algo como:
- Compare & Pull Request
- Você escolhe:
- base: main
- compare: minha-feature
