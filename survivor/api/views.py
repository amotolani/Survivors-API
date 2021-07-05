import logging
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Passenger
from .serializers import PassengerSerializer


logger = logging.getLogger(__name__)  # setup logger


# Create your views here.
class PassengerList(APIView):
    def get(self, request):
        """
        Fetch all Passengers data
        :param request: HTTP request
        :return:
        """
        passengers = Passenger.objects.all()
        serializer = PassengerSerializer(passengers, many=True)
        logger.info(msg="Getting all passenger records")
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Add Passenger to Database record
        :param request: HTTP Request
        :return:
        """
        data = request.data
        serializer = PassengerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info(msg="New passenger information saved. Passenger name is {}".format(serializer.data["name"]))
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.warning(msg='Failed to save new passenger information. Passenger name: {}. Failure reason: {}'.format(serializer.data["name"], serializer.errors))
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PassengerDetail(APIView):
    def verify_passenger(self, uuid):
        """
        Verify that a passenger with the provided UUID exists
        :param uuid: Unique Passenger UUID on the database
        :return: verified_passenger object
        """
        try:
            logger.info(msg='Attempting to get passenger details with uuid: {}'.format(uuid))
            verified_passenger = Passenger.objects.get(uuid=uuid)
            logger.info(msg='Passenger with uuid: {} is on record. Passenger name: {}'.format(uuid, verified_passenger))
            return verified_passenger
        except Exception:
            logger.warning(msg='No passenger on record with uuid: {}'.format(uuid))
            raise Http404

    def get(self, request, uuid):
        """
        Retrieve Details of the passenger with the the provided unique UUID
        :param request: Http Request
        :param uuid: Unique Passenger UUID on the database
        :return:
        """
        passenger = self.verify_passenger(uuid=uuid)
        serializer = PassengerSerializer(passenger)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, uuid):
        """
        Update details of passenger with the provided unique UUID
        :param request: HTTP Request
        :param uuid: Unique Passenger UUID on the database
        :return:
        """
        passenger = self.verify_passenger(uuid=uuid)
        serializer = PassengerSerializer(passenger, data=request.data)
        if serializer.is_valid():  # verify that serialized data is valid json
            serializer.save()  # save data
            logger.info(msg='Record updated for Passenger with uuid: {}. Passenger name: {}'.format(uuid, passenger))
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger.warning(msg='Update for Passenger with uuid: {} failed. Passenger name: {}. Failure reason: {}'.format(uuid, passenger, serializer.errors))
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        """
        Delete Passenger from Database
        :param request: Http Request
        :param uuid: Unique Passenger UUID on the database
        :return:
        """
        passenger = self.verify_passenger(uuid=uuid)
        passenger.delete()  # delete data
        logger.info(msg='Record deleted for Passenger with uuid: {}. Passenger name: {}'.format(uuid, passenger))
        return Response(status=status.HTTP_200_OK)


class Ping(APIView):
    def get(self, request):
        """
        Root route. Lets us know that the server is up and running
        :param request: HTTP request
        :return:
        """
        data = {
            'message': 'server is running'
        }
        return Response(data=data, status=status.HTTP_200_OK)
