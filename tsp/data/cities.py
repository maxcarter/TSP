import math

# City data obtained from:
# https://www.infoplease.com/world/united-states-geography/latitude-and-longitude-us-and-canadian-cities
cities = {
    'Albany, N.Y.': (42.40, 73.45),
    'Albuquerque, N.M.': (35.05, 106.39),
    'Amarillo, Tex.': (35.11, 101.50),
    'Anchorage, Alaska': (61.13, 149.54),
    'Atlanta, Ga.': (33.45, 84.23),
    'Austin, Tex.': (30.16, 97.44),
    'Baker, Ore.': (44.47, 117.50),
    'Baltimore, Md.': (39.18, 76.38),
    'Bangor, Maine': (44.48, 68.47),
    'Birmingham, Ala.': (33.30, 86.50),
    'Bismarck, N.D.': (46.48, 100.47),
    'Boise, Idaho': (43.36, 116.13),
    'Boston, Mass.': (42.21, 71.5),
    'Buffalo, N.Y.': (42.55, 78.50),
    'Calgary, Alba., Can.': (51.1, 114.1),
    'Carlsbad, N.M.': (32.26, 104.15),
    'Charleston, S.C.': (32.47, 79.56),
    'Charleston, W. Va.': (38.21, 81.38),
    'Charlotte, N.C.': (35.14, 80.50),
    'Cheyenne, Wyo.': (41.9, 104.52),
    'Chicago, Ill.': (41.50, 87.37),
    'Cincinnati, Ohio': (39.8, 84.30),
    'Cleveland, Ohio': (41.28, 81.37),
    'Columbia, S.C.': (34.0, 81.2),
    'Columbus, Ohio': (40.0, 83.1),
    'Dallas, Tex.': (32.46, 96.46),
    'Denver, Colo.': (39.45, 105.0),
    'Des Moines, Iowa': (41.35, 93.37),
    'Detroit, Mich.': (42.20, 83.3),
    'Dubuque, Iowa': (42.31, 90.40),
    'Duluth, Minn.': (46.49, 92.5),
    'Eastport, Maine': (44.54, 67.0),
    'Edmonton, Alb., Can.': (53.34, 113.28),
    'El Centro, Calif.': (32.38, 115.33),
    'El Paso, Tex.': (31.46, 106.29),
    'Eugene, Ore.': (44.3, 123.5),
    'Fargo, N.D.': (46.52, 96.48),
    'Flagstaff, Ariz.': (35.13, 111.41),
    'Fort Worth, Tex.': (32.43, 97.19),
    'Fresno, Calif.': (36.44, 119.48),
    'Grand Junction, Colo.': (39.5, 108.33),
    'Grand Rapids, Mich.': (42.58, 85.40),
    'Havre, Mont.': (48.33, 109.43),
    'Helena, Mont.': (46.35, 112.2),
    'Honolulu, Hawaii': (21.18, 157.50),
    'Hot Springs, Ark.': (34.31, 93.3),
    'Houston, Tex.': (29.45, 95.21),
    'Idaho Falls, Idaho': (43.30, 112.1),
    'Indianapolis, Ind.': (39.46, 86.10),
    'Jackson, Miss.': (32.20, 90.12),
    'Jacksonville, Fla.': (30.22, 81.40),
    'Juneau, Alaska': (58.18, 134.24),
    'Kansas City, Mo.': (39.6, 94.35),
    'Key West, Fla.': (24.33, 81.48),
    'Kingston, Ont., Can.': (44.15, 76.30),
    'Klamath Falls, Ore.': (42.10, 121.44),
    'Knoxville, Tenn.': (35.57, 83.56),
    'Las Vegas, Nev.': (36.10, 115.12),
    'Lewiston, Idaho': (46.24, 117.2),
    'Lincoln, Neb.': (40.50, 96.40),
    'London, Ont., Can.': (43.2, 81.34),
    'Long Beach, Calif.': (33.46, 118.11),
    'Los Angeles, Calif.': (34.3, 118.15),
    'Louisville, Ky.': (38.15, 85.46),
    'Manchester, N.H.': (43.0, 71.30),
    'Memphis, Tenn.': (35.9, 90.3),
    'Miami, Fla.': (25.46, 80.12),
    'Milwaukee, Wis.': (43.2, 87.55),
    'Minneapolis, Minn.': (44.59, 93.14),
    'Mobile, Ala.': (30.42, 88.3),
    'Montgomery, Ala.': (32.21, 86.18),
    'Montpelier, Vt.': (44.15, 72.32),
    'Montreal, Que., Can.': (45.30, 73.35),
    'Moose Jaw, Sask., Can.': (50.37, 105.31),
    'Nashville, Tenn.': (36.10, 86.47),
    'Nelson, B.C., Can.': (49.30, 117.17),
    'Newark, N.J.': (40.44, 74.10),
    'New Haven, Conn.': (41.19, 72.55),
    'New Orleans, La.': (29.57, 90.4),
    'New York, N.Y.': (40.47, 73.58),
    'Nome, Alaska': (64.25, 165.30),
    'Oakland, Calif.': (37.48, 122.16),
    'Oklahoma City, Okla.': (35.26, 97.28),
    'Omaha, Neb.': (41.15, 95.56),
    'Ottawa, Ont., Can.': (45.24, 75.43),
    'Philadelphia, Pa.': (39.57, 75.10),
    'Phoenix, Ariz.': (33.29, 112.4),
    'Pierre, S.D.': (44.22, 100.21),
    'Pittsburgh, Pa.': (40.27, 79.57),
    'Portland, Maine': (43.40, 70.15),
    'Portland, Ore.': (45.31, 122.41),
    'Providence, R.I.': (41.50, 71.24),
    'Quebec, Que., Can.': (46.49, 71.11),
    'Raleigh, N.C.': (35.46, 78.39),
    'Reno, Nev.': (39.30, 119.49),
    'Richfield, Utah': (38.46, 112.5),
    'Richmond, Va.': (37.33, 77.29),
    'Roanoke, Va.': (37.17, 79.57),
    'Sacramento, Calif.': (38.35, 121.30),
    'St. John, N.B., Can.': (45.18, 66.10),
    'St. Louis, Mo.': (38.35, 90.12),
    'Salt Lake City, Utah': (40.46, 111.54),
    'San Antonio, Tex.': (29.23, 98.33),
    'San Diego, Calif.': (32.42, 117.10),
    'San Francisco, Calif.': (37.47, 122.26),
    'San Jose, Calif.': (37.20, 121.53),
    'San Juan, P.R.': (18.30, 66.10),
    'Santa Fe, N.M.': (35.41, 105.57),
    'Savannah, Ga.': (32.5, 81.5),
    'Seattle, Wash.': (47.37, 122.20),
    'Shreveport, La.': (32.28, 93.42),
    'Sioux Falls, S.D.': (43.33, 96.44),
    'Sitka, Alaska': (57.10, 135.15),
    'Spokane, Wash.': (47.40, 117.26),
    'Springfield, Ill.': (39.48, 89.38),
    'Springfield, Mass.': (42.6, 72.34),
    'Springfield, Mo.': (37.13, 93.17),
    'Syracuse, N.Y.': (43.2, 76.8),
    'Tampa, Fla.': (27.57, 82.27),
    'Toledo, Ohio': (41.39, 83.33),
    'Toronto, Ont., Can.': (43.40, 79.24),
    'Tulsa, Okla.': (36.09, 95.59),
    'Vancouver, B.C., Can.': (49.13, 123.06),
    'Victoria, B.C., Can.': (48.25, 123.21),
    'Virginia Beach, Va.': (36.51, 75.58),
    'Washington, D.C.': (38.53, 77.02),
    'Wichita, Kan.': (37.43, 97.17),
    'Wilmington, N.C.': (34.14, 77.57),
    'Winnipeg, Man., Can.': (49.54, 97.7)
}


class Cities:
    def getData(self):
        return cities

    def calculate_distance(a, b):
        earth_radius = 3963
        latitude_a, longitude_a = math.radians(a[0]), math.radians(a[1])
        latitude_b, longitude_b = math.radians(b[0]), math.radians(b[1])

        sin = math.sin(latitude_a) + math.sin(latitude_b)
        cos = math.cos(latitude_a) + math.cos(latitude_b)

        distance = math.acos(
            sin + cos + math.cos(longitude_a - longitude_b)) * earth_radius

        return distance

    def generate_distance_matrix(self):
        distance_matrix = {}
        for k1, v1 in cities.items():
            distance_matrix[k1] = {}
            for k2, v2 in cities.items():
                if k2 == k1:
                    distance_matrix[k1][k2] = 0.0
                else:
                    distance_matrix[k1][k2] = self.calculate_distance(v1, v2)
        return distance_matrix
