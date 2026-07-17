import pytest
from generator import PasswordGenerator


class TestPasswordGenerator:
    def test_default_init(self):
        gen = PasswordGenerator()
        assert gen.length == 0
        assert gen.seed_seq is None
        assert gen.pw == ""
        assert gen.check is False

    def test_init_with_params(self):
        gen = PasswordGenerator(length=10, seed_seq="test", pw="existing", check=True)
        assert gen.length == 10
        assert gen.seed_seq == "test"
        assert gen.pw == "existing"
        assert gen.check is True

    def test_generate_password_deterministic(self):
        gen1 = PasswordGenerator(length=15, seed_seq="myseed")
        gen1.generate_password()

        gen2 = PasswordGenerator(length=15, seed_seq="myseed")
        gen2.generate_password()

        assert gen1.pw == gen2.pw

    def test_generate_password_different_seeds_different_output(self):
        gen1 = PasswordGenerator(length=15, seed_seq="seed1")
        gen1.generate_password()

        gen2 = PasswordGenerator(length=15, seed_seq="seed2")
        gen2.generate_password()

        assert gen1.pw != gen2.pw

    def test_generate_password_different_lengths(self):
        gen1 = PasswordGenerator(length=10, seed_seq="same")
        gen1.generate_password()

        gen2 = PasswordGenerator(length=20, seed_seq="same")
        gen2.generate_password()

        assert len(gen1.pw) == 10
        assert len(gen2.pw) == 20
        assert gen1.pw != gen2.pw

    def test_generate_password_min_length(self):
        gen = PasswordGenerator(length=4, seed_seq="test")
        gen.generate_password()
        assert len(gen.pw) == 4

    def test_generate_password_max_length(self):
        gen = PasswordGenerator(length=72, seed_seq="test")
        gen.generate_password()
        assert len(gen.pw) == 72

    def test_check_good_pw_strong(self):
        gen = PasswordGenerator(length=15, seed_seq="strongseed123!@#")
        gen.generate_password()
        gen.check_good_pw()

        assert gen.check is True

    def test_check_good_pw_weak_no_upper(self):
        gen = PasswordGenerator(pw="lowercase123!")
        gen.check_good_pw()
        assert gen.check is False

    def test_check_good_pw_weak_no_lower(self):
        gen = PasswordGenerator(pw="UPPERCASE123!")
        gen.check_good_pw()
        assert gen.check is False

    def test_check_good_pw_weak_no_number(self):
        gen = PasswordGenerator(pw="NoNumbers!")
        gen.check_good_pw()
        assert gen.check is False

    def test_check_good_pw_weak_no_special(self):
        gen = PasswordGenerator(pw="NoSpecial123")
        gen.check_good_pw()
        assert gen.check is False

    def test_check_good_pw_empty(self):
        gen = PasswordGenerator(pw="")
        gen.check_good_pw()
        assert gen.check is False

    def test_character_set_includes_all_types(self):
        gen = PasswordGenerator(length=72, seed_seq="test")
        gen.generate_password()

        has_upper = any(c.isupper() for c in gen.pw)
        has_lower = any(c.islower() for c in gen.pw)
        has_digit = any(c.isdigit() for c in gen.pw)
        has_special = any(c in "!@#$%&*()_" for c in gen.pw)

        assert has_upper
        assert has_lower
        assert has_digit
        assert has_special


class TestCLI:
    def test_cli_help(self):
        import subprocess
        result = subprocess.run(["python", "cli.py", "--help"], capture_output=True, text=True)
        assert result.returncode == 0
        assert "seed" in result.stdout.lower()

    def test_cli_generate(self):
        import subprocess
        result = subprocess.run(["python", "cli.py", "-s", "testseed", "-l", "15"], capture_output=True, text=True)
        assert result.returncode == 0
        assert len(result.stdout.strip()) == 15

    def test_cli_generate_with_check(self):
        import subprocess
        result = subprocess.run(["python", "cli.py", "-s", "testseed", "-l", "15", "-c"], capture_output=True, text=True)
        assert result.returncode == 0
        assert len(result.stdout.strip()) == 15
        assert "Strength:" in result.stderr

    def test_cli_invalid_length(self):
        import subprocess
        result = subprocess.run(["python", "cli.py", "-s", "test", "-l", "3"], capture_output=True, text=True)
        assert result.returncode == 1
        assert "Error" in result.stderr