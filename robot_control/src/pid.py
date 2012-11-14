#!/usr/bin/env python

# PID (Proportional, Integral, Derivative) controller implementation in Python for feedback control of robot


class Controller():
	_integral = 0.0
	_prev_err = 0.0

	# Tuning parameters
	k_p = 1.0
	k_i = 1.0
	k_d = 1.0

	# If there's a long pause, reset to avoid control spikes
	max_timestep = 1.0

	def control(self, actual, target, dt):
		if dt > max_timestep:
			_integral = 0.0
			_prev_err = 0.0
			dt = 0
		err = target - actual
		self._integral += err * dt
		deriv = (err - self._prev_err)

		rV = k_p * error + k_i * self._integral + k_d * deriv

		self._prev_err = err
		return rV


