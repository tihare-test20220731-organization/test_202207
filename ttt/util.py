import numpy as np
from typing import Union


class Util:
    """
    Bundle class of static methods.
    """

    @staticmethod
    def add(lhs: np.ndarray, rhs: np.ndarray) -> np.ndarray:
        """
        Add method.

        Args:
            lhs: left hand side.
            rhs: right hand side.
        Returns:
            added value.

        """
        return lhs + rhs

    @staticmethod
    def sub(
        lhs: Union[np.ndarray, None], rhs: np.ndarray, *args, **kwargs
    ) -> np.ndarray:
        """
        Sub method.

        Args:
            lhs: left hand side.
            rhs: right hand side.
        Returns:
            subtracted value.

        """
        if lhs is None:
            lhs = np.array([0, 0, 0])

        return lhs - rhs


    @staticmethod
    def mult(
        lhs: float, rhs: np.ndarray, *args, **kwargs
    ) -> np.ndarray:
        """
        Mult method.

        Args:
            lhs: coef
            rhs: right hand side.
        Returns:
            multiplied value.

        """
        if not isinstance(lhs, float):
            raise Exception()

        if not isinstance(rhs, np.ndarray):
            raise Exception()
            
        return lhs * rhs
