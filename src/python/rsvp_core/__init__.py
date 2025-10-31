"""
RSVP Core — Relativistic Scalar-Vector Plenum
Shared utilities for field dynamics, gauge theory, and coherence.
"""
from .fields import RSVPFields
from .lagrangian import Lagrangian
from .solitons import AbelianVortex, Monopole

__all__ = ['RSVPFields', 'Lagrangian', 'AbelianVortex', 'Monopole']
