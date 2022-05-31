from enum import Enum


class AdministrativeDepartment(Enum):
    sociocultural_management_and_promotion_department = "Área de Gestión y Promoción Sociocultural"
    course_department = "Área de Cursos"
    secretary_department = "Área de Secretaría"
    surveillance_and_security_department = "Área de Vigilancia y Seguridad"
    janitor_department = "Área de Conserjería"
    coordination_department = "Coordinación"


class TeachingDepartment(Enum):
    performing_arts_department = "Artes Escénicas"
    costa_rican_sign_language_department = "Lengua de Señas Costarricense"
    manual_arts_department = "Artes Manuales"
    musical_arts_department = "Artes Musicales"
    art_and_health_department = "Arte y Salud"
    visual_arts_department = "Artes Visuales"
