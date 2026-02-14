# src/ciphers/ecc_system.py

class EllipticCurve:
    """Represents an elliptic curve y^2 = x^3 + ax + b (mod p)."""
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def is_on_curve(self, x, y):
        """Checks if a point (x, y) lies on the curve."""
        if x is None: return True  # Point at infinity
        return (y**2 - (x**3 + self.a * x + self.b)) % self.p == 0

    def point_addition(self, P, Q):
        """Adds two points P and Q on the curve."""
        if P is None: return Q
        if Q is None: return P
        
        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and (y1 != y2 or y1 == 0):
            return None  # Point at infinity

        if x1 == x2:
            # Point doubling
            m = (3 * x1**2 + self.a) * pow(2 * y1, -1, self.p)
        else:
            # Point addition
            m = (y2 - y1) * pow(x2 - x1, -1, self.p)

        m %= self.p
        x3 = (m**2 - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def scalar_multiplication(self, k, P):
        """Computes k * P using the double-and-add algorithm."""
        result = None
        addend = P
        while k:
            if k & 1:
                result = self.point_addition(result, addend)
            addend = self.point_addition(addend, addend)
            k >>= 1
        return result

class ECCUser:
    """Represents a user (like Tim or Stephen) in the ECDH exchange."""
    def __init__(self, name, curve, base_point, private_key):
        self.name = name
        self.curve = curve
        self.base_point = base_point
        self.private_key = private_key
        # Public Key = private_key * Base_Point
        self.public_key = self.curve.scalar_multiplication(private_key, base_point)

    def compute_shared_secret(self, other_public_key):
        """Shared Secret = my_private_key * other_public_key."""
        return self.curve.scalar_multiplication(self.private_key, other_public_key)