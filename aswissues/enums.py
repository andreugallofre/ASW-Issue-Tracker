from enum import Enum


class TipusSelector(Enum):   # A subclass of Enum
    Bug = "Bug"
    Millora = "Millora"
    Proposta = "Proposta"
    Tasca = "Tasca"


class PrioritatSelector(Enum):   # A subclass of Enum
    Trivial = "Trivial"
    Menor = "Menor"
    Major = "Major"
    Critica = "Crítica"
    Bloquejant = "Bloquejant"


class StatusSelector(Enum):
    Nou = "Nou"
    Obert = "Obert"
    Resolt = "Resolt"
    Espera = "En Espera"
    Invalit = "Invalit"
    Duplicat = "Duplicat"
    NoFix = "No fix"
    Tancat = "Tancat"
