
import pytest
import PrimeNumberProgram as pp


class TestPrimeGenerators:
    """Sieve of Eratosthenes and Sieve of Atkin."""

    @classmethod
    def setup_class(cls):
        cls.PRIMES_TO_50 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    def setup_method(self, method):
        self.limit = 50                     # fresh input for every test

    def test_eratosthenes_returns_known_primes(self):
        assert pp.sieve_of_eratosthenes(self.limit) == self.PRIMES_TO_50

    def test_eratosthenes_below_two_is_empty(self):
        for n in (-5, 0, 1):
            assert pp.sieve_of_eratosthenes(n) == []

    def test_eratosthenes_includes_limit_when_prime(self):
        assert pp.sieve_of_eratosthenes(13)[-1] == 13

    def test_atkin_returns_known_primes(self):
        assert pp.sieve_of_atkin(self.limit) == self.PRIMES_TO_50

    def test_atkin_edge_limits(self):
        assert pp.sieve_of_atkin(0) == []
        assert pp.sieve_of_atkin(1) == []
        assert pp.sieve_of_atkin(2) == [2]
        assert pp.sieve_of_atkin(3) == [2, 3]

    def test_atkin_matches_eratosthenes(self):
        for limit in (10, 100, 1000):
            assert pp.sieve_of_atkin(limit) == pp.sieve_of_eratosthenes(limit)


class TestPrimalityAndRanges:
    """Trial division, range search, and timing wrappers."""

    def setup_method(self, method):
        self.primes = [2, 3, 5, 7, 97]
        self.non_primes = [-7, 0, 1, 4, 9, 25, 100]   # includes perfect squares

    def test_trial_division_identifies_primes(self):
        for n in self.primes:
            assert pp.trail_Devision(n) is True

    def test_trial_division_rejects_non_primes(self):
        for n in self.non_primes:
            assert pp.trail_Devision(n) is False

    def test_trial_division_agrees_with_sieve(self):
        sieve = set(pp.sieve_of_eratosthenes(200))
        for n in range(0, 201):
            assert pp.trail_Devision(n) == (n in sieve)

    def test_primes_in_range_returns_primes_and_elapsed_time(self):
        primes, elapsed = pp.primes_in_range_with_time(10, 30)
        assert primes == [11, 13, 17, 19, 23, 29]
        assert elapsed >= 0

    def test_range_start_below_two_is_clamped(self):
        primes, _ = pp.primes_in_range_with_time(-5, 10)
        assert primes == [2, 3, 5, 7]

    def test_invalid_ranges_return_empty_and_zero(self):
        assert pp.primes_in_range_with_time(20, 10) == ([], 0.0)   # start > end
        assert pp.primes_in_range_with_time(0, 1) == ([], 0.0)     # nothing >= 2

    def test_atkin_timed_returns_primes_and_reports_count(self, capsys):
        primes, elapsed = pp.atkin_timed(10)
        assert primes == [2, 3, 5, 7]
        assert elapsed >= 0
        assert "found 4 primes up to 10" in capsys.readouterr().out

    @pytest.mark.xfail(strict=True,
                       reason="known bug: generate_test_cases builds temp_list "
                              "but never returns it (returns None)")
    def test_generate_test_cases_returns_list_of_requested_size(self):
        result = pp.generate_test_cases(5, 2, 4)
        assert isinstance(result, list) and len(result) == 5
