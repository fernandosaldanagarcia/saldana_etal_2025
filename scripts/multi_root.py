from typing import Callable, Iterable
import numpy as np
from scipy.optimize import root_scalar

def multi_root(f: Callable, bracket: Iterable[float], args: Iterable = (), n: int = 30) -> np.ndarray:
    """
    Identify all real roots of the function `f` within the interval `bracket`, assuming the sampling resolution `n` is sufficient to detect all sign changes.

    Root detection is refined using `scipy.optimize.root_scalar`.

    Parameters
    ----------
    f : Callable
        The target function for which roots are to be found.
    bracket : Sequence[float]
        A two-element sequence specifying the interval within which to search for roots.
    args : Iterable, optional
        Additional arguments to pass to the function `f` during evaluation.
    n : int
        Number of evenly spaced sample points used to probe the interval. The resolution must be fine enough to capture every sign change corresponding to a root, but should not be excessively high.

    Returns
    -------
    roots : np.ndarray
        A NumPy array containing all distinct roots located within the specified interval.
    """
    # Evaluate function in given bracket
    x = np.linspace(*bracket, n)
    y = f(x, *args)

    # Find where adjacent signs are not equal
    sign_changes = np.where(np.sign(y[:-1]) != np.sign(y[1:]))[0]

    # Find roots around sign changes
    root_finders = (
        root_scalar(
            f=f,
            args=args,
            bracket=(x[s], x[s+1])
        )
        for s in sign_changes
    )

    roots = np.array([
        r.root if r.converged else np.nan
        for r in root_finders
    ])

    # Drop non-converged results
    roots = roots[~np.isnan(roots)]

    # Drop duplicates
    roots_unique = np.unique(roots)

    return roots_unique



